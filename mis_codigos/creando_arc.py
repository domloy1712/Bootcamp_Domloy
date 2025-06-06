import os

ruta = 'C:\\Users\\Matins\\Desktop\\Prueba'

def crear_arcivos(ruta):
    for i in range(100):
        nombre = f'{i}.txt'
        ruta_completa = os.path.join(ruta, nombre)
        open(ruta_completa, 'w').close()
    print(f'Creado arcivo {i}.txt')

def modificar_nombre(ruta):
    for i in range(100):
        nombre = '.txt'
        ruta_completa = os.path.join(ruta, nombre)
        nuevo_nombre = f'Esta guapo esto_{i}.txt'
        nueva_ruta = os.path.join(ruta, nuevo_nombre)
        os.rename(ruta_completa, nueva_ruta)
        print(f'Modificado arcivo {nombre} a {nuevo_nombre}')

def eliminar_arcivos(ruta):
    for i in range(100):
        nombre = f'{i}.txt'
        ruta_completa = os.path.join(ruta, nombre)
        if os.path.exists(ruta_completa):
            os.remove(ruta_completa)
            print(f'Eliminado arcivo {nombre}')
        else:
            print(f'No existe el arcivo {nombre}')


modificar_nombre(ruta)