from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json

lista_productos = {
  'tienda': 'Gato Arcano',
  'productos': [],
}

def obtener_productos(soup):
  productos = soup.find_all('div', class_='bs-collection__product border')
  
   
  for producto in productos:
    nombre = producto.find('h3').text.strip()
    url = f'https://www.laloseta.cl{producto.find('a').get('href')}'
    cover = producto.find('img').get('src')
    
    if producto.find('div', class_='bs-collection__product-stock'):
      continue
    else:
      precio = producto.find('strong').text.strip()    

    juego = {'nombre': nombre, 'precio': precio, 'url': url, 'cover': cover}
    
    lista_productos['productos'].append(juego)
  
  
  return lista_productos
  
def main():
  url = f'https://www.laloseta.cl/collection/todos-los-juegos'
  
  driver=webdriver.Chrome()
  driver.get(url)

  driver.implicitly_wait(10)
  
  ultima_pagina = int(driver.find_element(By.CSS_SELECTOR, 'ul.pagination li.page-item:nth-last-child(2) a.page-link').text)
  
  print(ultima_pagina)
  
  for pagina in range (1, ultima_pagina + 1):
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    
    obtener_productos(soup)
    
    if pagina < ultima_pagina:    
      next_button = driver.find_element(By.CSS_SELECTOR, 'ul.pagination li.page-item:last-child a.page-link')
      next_button.click()
      driver.implicitly_wait(10)
  
  driver.quit()    
  
  with open('./json/laloseta.json', 'w', encoding='utf-8') as json_file:
    json.dump(lista_productos, json_file, ensure_ascii=False, indent=2)   
  

if __name__ == "__main__":
    main()