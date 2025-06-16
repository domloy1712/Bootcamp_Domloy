class Pelicula:
    def __init__(self, id, titulo, disponble=True):
        self.id = id
        self.titulo=titulo
        self.disponible=disponble

class Cliente:
    def __init__(self,id , nombre):
        self.id = id
        self.nombre = nombre

class Alquiler():
    def __init__(self, id,cliente_id,pelicula_id, fecha,devuelto=False):
        self.id = id
        self.cliente_id = cliente_id
        self.pelicula_id = pelicula_id
        self.fecha = fecha
        self.devuelto = devuelto

