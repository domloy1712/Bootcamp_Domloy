import os

ruta = 'C:\\Users\\Matins\\Desktop\\Prueba.txt'
nombre = 'C:\\Users\\Matins\\Desktop\\ola.txt'

def cambiar():
      os.rename(ruta,nombre)

cambiar()