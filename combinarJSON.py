import json
import os

def combinar_archivos():

  todos_los_productos = []

  json_directory = './json/'

  for json_file in os.listdir(json_directory):
    if json_file.endswith('.json'):
      ruta_archivo = os.path.join(json_directory, json_file)
      
      with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        datos_archivo = json.load(archivo)
        
        todos_los_productos.append(datos_archivo)
        
  with open('todos_los_productos.json', 'w', encoding='utf-8') as resultado:
    json.dump(todos_los_productos, resultado, ensure_ascii=False, indent=2)
