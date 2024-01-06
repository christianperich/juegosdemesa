from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json

lista_productos = []

def obtener_productos(soup):
  productos = soup.find_all('li', class_='product')
    
  for producto in productos:    
    nombre = producto.find('h2').text    
    url = producto.find('a').get('href')
    cover = producto.find('img').get('src')
    
    precio = producto.find('span', class_='price').text
    
    juego = {'nombre': nombre, 'precio': precio, 'url': url, 'cover': cover}
    
    lista_productos.append(juego)
  
  return lista_productos
       


def main():
  url = 'https://www.comercialsmc.cl/categoria-producto/juegos-de-mesa/'
  
  driver=webdriver.Chrome()  
  driver.get(url)

  driver.implicitly_wait(10)
  
  html = driver.page_source
  soup = BeautifulSoup(html, 'lxml')
      
  obtener_productos(soup)
  
  driver.implicitly_wait(10)    
  
  driver.quit()

 
  with open('./json/comercialsmc.json', 'w', encoding='utf-8') as json_file:
    json.dump(lista_productos, json_file, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()