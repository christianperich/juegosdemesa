from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver=webdriver.Chrome()

url = 'https://gatoarcano.cl/product-category/juegos-de-mesa/'
driver.get(url)

driver.implicitly_wait(10)

for pagina in range (1, 3):
  
  html = driver.page_source
  soup = BeautifulSoup(html, 'lxml')
  
  productos = soup.find_all('li', class_='product')
    
  for producto in productos:    
    nombre = producto.find('h2').text
    
    if producto.find('span', class_='now_sold'):
      pass
    elif producto.find('span', class_='onsale'):
      precio = producto.find('ins').text
      print(f'{nombre}: // Precio: {precio}')    
    else:
      precio = producto.find('span', class_='price').text
      print(f'{nombre}: // Precio: {precio}')
    
  next_button = driver.find_element(By.CLASS_NAME, 'next')
  driver.execute_script("arguments[0].click();", next_button)
  driver.implicitly_wait(10)    
       
driver.quit()