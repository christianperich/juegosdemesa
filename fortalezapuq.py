from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver=webdriver.Chrome()

url = f'https://www.lafortalezapuq.cl/jdm?page=1'
driver.get(url)

driver.implicitly_wait(10)


for pagina in range (1,3):
  html = driver.page_source
  soup = BeautifulSoup(html, 'lxml')
  
  productos = soup.find_all('figure', class_='product')
  
  for producto in productos:
    nombre = producto.find('h5').text
    
    if producto.find('div', class_='product-out-of-stock'):
      pass
    elif producto.find('i'):
      precio = producto.find('i').text
    else:
      precio = producto.find('span', class_='product-price').text
  
    print(f'{nombre} // Precio: {precio}')
  
  next_button = driver.find_element(By.CLASS_NAME, 'next')
  driver.execute_script("arguments[0].click();", next_button)
  driver.implicitly_wait(10)
        
driver.quit()