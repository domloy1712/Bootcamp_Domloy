import requests
from bs4 import BeautifulSoup
import csv 
import schedule

info = []
url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'

def pasarlo_a_csv(filename,info):
    with open( filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Precio'])  # Escribir encabezados
        writer.writerows(info)

def cada_cierto_tiempo(url):
    schedule.every(60).seconds.do(lambda: scrapear(url))
    while True:
        schedule.run_pending()
        

def scrapear(url):
   responder = requests.get(url)
   if responder.status_code == 200:
        soup = BeautifulSoup(responder.text, 'html.parser')
        precio = soup.find('span', itemprop='price').text
        print(f'Precio actualizado: {precio}')
        pasarlo_a_csv('precios.csv', [[precio]])
   else:
        print(f'Error al acceder a la página: {responder.status_code}')

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'
pasarlo_a_csv('Precios.csv', info)
cada_cierto_tiempo(url)
