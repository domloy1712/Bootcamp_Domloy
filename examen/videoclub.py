from db_manager import DBManager

class VideoClub:
    def __init__(self):
        self.db = DBManager()
    
    def añadir_pelicula(self, titulo):
        self.db.agregar_pelicula(titulo)

    def mostrar_peliculas(self):
        peliculas = self.db.listar_peliculas()
        for p in peliculas:
            estado = "Disponible" if p.disponible else "Alquilada"
            print(f"{p.id}. {p.titulo} - {estado}")
    
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
        for h in self.db.historial():
            estado = "Devuelto" if h[4] else "En alquiler"
            print(f"[{h[0]}] {h[1]} alquiló '{h[2]}' el {h[3]} - {estado}")
