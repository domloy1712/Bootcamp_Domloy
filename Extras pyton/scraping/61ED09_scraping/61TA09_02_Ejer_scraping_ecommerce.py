import requests
from bs4 import BeautifulSoup
import csv

# URL de la página de laptops
url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'

# Realizar la solicitud GET
response = requests.get(url)

# Analizar el contenido HTML con BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar todos los contenedores de los productos
products = soup.find_all('div', class_='col-sm-4 col-lg-4 col-md-4')

# Crear una lista para almacenar los datos de los productos
product_data = []

# Extraer los datos de cada producto
for product in products:
    # Nombre del producto
    name = product.find('a', class_='title').text.strip()
    
    # Precio del producto
    price = product.find('h4', class_='price').text.strip()
    
    # Descripción del producto
    description = product.find('p', class_='description').text.strip()
    
    # Cantidad de reviews
    reviews = product.find('div', class_='ratings').find('p').text.strip()
    
    # Añadir los datos del producto a la lista
    product_data.append([name, price, description, reviews])

# Guardar los datos en un archivo CSV
with open('laptops_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Nombre', 'Precio', 'Descripción', 'Reseñas'])
    writer.writerows(product_data)

print("Datos de productos guardados en 'laptops_data.csv'")
