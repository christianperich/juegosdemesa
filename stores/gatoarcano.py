from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json

lista_productos = {
  'tienda': 'Gato Arcano',
  'productos': [],
}

def obtener_productos(soup):
  productos = soup.find_all('li', class_='product')
    
  for producto in productos:    
    nombre = producto.find('h2').text    
    url = producto.find('a').get('href')
    cover = producto.find('img').get('src')
    
    if producto.find('span', class_='now_sold'):
      continue
    elif producto.find('span', class_='onsale'):
      precio = producto.find('ins').text   
    else:
      precio = producto.find('span', class_='price').text
    
    juego = {'nombre': nombre, 'precio': precio, 'url': url, 'cover': cover}
    
    lista_productos['productos'].append(juego)
  
  return lista_productos
       

def main():
  url = 'https://gatoarcano.cl/product-category/juegos-de-mesa/'
  
  driver=webdriver.Chrome()  
  driver.get(url)

  driver.implicitly_wait(10)
  
  html = driver.page_source
  soup = BeautifulSoup(html, 'lxml')
  
  driver.implicitly_wait(10)
  
  total_paginas = 36
  
  print(total_paginas)
      
  for pagina in range (1, total_paginas + 1):  
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    
    obtener_productos(soup)
    
    if pagina < total_paginas:
      next_button = driver.find_element(By.CLASS_NAME, 'next')
      driver.execute_script("arguments[0].click();", next_button)
      driver.implicitly_wait(10)    
  
  driver.quit()

 
  with open('./json/gatoarcano.json', 'w', encoding='utf-8') as json_file:
    json.dump(lista_productos, json_file, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()