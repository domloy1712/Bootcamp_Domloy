from db_manager import DBManager
import csv


def exportar_alquileres_a_csv(nombre_archivo="eloy.csv"):
       db = DBManager()
       historial = db.historial()
        
       with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["ID", "Cliente", "Película", "Fecha","Devuelto"])

            for fila in historial:
               writer.writerow(fila)