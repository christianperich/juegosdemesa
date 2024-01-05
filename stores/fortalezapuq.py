from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json

lista_productos = []

def obtener_productos(soup):
  productos = soup.find_all('figure', class_='product')
  
   
  for producto in productos:
    nombre = producto.find('h5').text
    url = f'https://www.lafortalezapuq.cl{producto.find('a').get('href')}'
    cover = producto.find('img').get('src')
    
    if producto.find('div', class_='product-out-of-stock'):
      continue
    elif producto.find('i'):
      precio = producto.find('i').text
    else:
      precio = producto.find('span', class_='product-price').text

    juego = {'nombre': nombre, 'precio': precio, 'url': url, 'cover': cover}
    
    lista_productos.append(juego)
  
  
  return lista_productos
  
def main():
  url = f'https://www.lafortalezapuq.cl/jdm?page=1'
  
  driver=webdriver.Chrome()
  driver.get(url)

  driver.implicitly_wait(10)
  
  total_paginas = 67
  
  for pagina in range (1, total_paginas + 1):
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    
    obtener_productos(soup)
    
    if pagina < total_paginas:    
      next_button = driver.find_element(By.CLASS_NAME, 'next')
      driver.execute_script("arguments[0].click();", next_button)
      driver.implicitly_wait(10)
  
  driver.quit()    
  
  with open('fortalezapuq.json', 'w', encoding='utf-8') as json_file:
    json.dump(lista_productos, json_file, ensure_ascii=False, indent=2)   
  

if __name__ == "__main__":
    main()