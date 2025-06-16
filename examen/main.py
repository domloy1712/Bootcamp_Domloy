from videoclub import VideoClub
from exportar import exportar_alquileres_a_csv


def menu():
    v = VideoClub()
    
    while True:
        print("\n🎬 VIDEOCLUB")
        print("1. Añadir película")
        print("2. Ver películas")
        print("3. Registrar cliente")
        print("4. Alquilar película")
        print("5. Devolver película")
        print("6. Ver historial")
        print("7. exportar a CSV")
        print("8. Salir")
        op = input("Opción: ")

        if op == "1":
            v.añadir_pelicula(input("Título: "))
        elif op == "2":
            v.mostrar_peliculas()
        elif op == "3":
            v.registrar_cliente(input("Nombre: "))
        elif op == "4":
            v.alquilar(int(input("ID cliente: ")), int(input("ID película: ")))
        elif op == "5":
            v.devolver(int(input("ID película: ")))
        elif op == "6":
            v.mostrar_historial()
        elif op == "7":
            print("Exportado")
            exportar_alquileres_a_csv()
        elif op == "8":
            break
        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    menu()