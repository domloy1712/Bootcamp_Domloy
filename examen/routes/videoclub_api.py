from db_manager import DBManager

class VideoClub:
    def __init__(self):
        self.db = DBManager()
    
    def añadir_pelicula(self, titulo):
        self.db.agregar_pelicula(titulo)

    def mostrar_peliculas(self):
        peliculas = self.db.listar_peliculas()
        resultado = []
        for p in peliculas:
            estado = "Disponible" if p.disponible else "Alquilada"
            resultado.append({
            "id": p.id,
            "titulo": p.titulo,
            "estado": estado
        })
        return resultado
        
    
    def registrar_cliente(self, nombre):
        self.db.registrar_cliente(nombre)

    def alquilar(self, cliente_id, pelicula_id):
        if self.db.alquilar_pelicula(cliente_id, pelicula_id):
            print("Alquiler realizado")
        else:
            print("Pelicula no disponible")

    def devolver(self, pelicula_id):
        self.db.devolver_pelicula(pelicula_id)
        print("Pelicula devuelta")

    def mostrar_historial(self):
        resultado = []
        for h in self.db.historial():
            estado = "Devuelto" if h[4] else "En alquiler"
            resultado.append({        
            "id": h[0],
            "cliente": h[1],
            "pelicula": h[2],
            "fecha": h[3],
            "estado": estado
        })
        return resultado 
            

