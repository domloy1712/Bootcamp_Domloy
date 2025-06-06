import sqlite3
import csv

def conectar():
    conexion = sqlite3.connect("agenda.db")
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT,
            email TEXT
        )
    ''')
    conexion.commit()
    conexion.close()

def agregar_contacto(nombre, telefono, email):
    conexion = sqlite3.connect("agenda.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO contactos (nombre, telefono, email) VALUES (?, ?, ?)",
                   (nombre, telefono, email))
    conexion.commit()
    conexion.close()

def listar_contactos():
    conexion = sqlite3.connect("agenda.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM contactos")
    contactos = cursor.fetchall()
    conexion.close()

    for contacto in contactos:
        print(f"ID: {contacto[0]}, Nombre: {contacto[1]}, Teléfono: {contacto[2]}, Email: {contacto[3]}")

def buscar_contacto(nombre):
    conexion = sqlite3.connect("agenda.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM contactos WHERE nombre LIKE ?", ('%' + nombre + '%',))
    resultados = cursor.fetchall()
    conexion.close()

    for contacto in resultados:
        print(f"ID: {contacto[0]}, Nombre: {contacto[1]}, Teléfono: {contacto[2]}, Email: {contacto[3]}")

def editar_contacto(id, nuevo_nombre, nuevo_telefono, nuevo_email):
    conexion = sqlite3.connect("agenda.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE contactos SET nombre = ?, telefono = ?, email = ? WHERE id = ?",
                   (nuevo_nombre, nuevo_telefono, nuevo_email, id))
    conexion.commit()
    conexion.close()


def eliminar_contacto(id):
    conexion = sqlite3.connect("agenda.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM contactos WHERE id = ?", (id))
    conexion.commit()
    conexion.close()

def menu():
    while True:
        print("\n📒 Agenda de Contactos")
        print("1. Agregar contacto")
        print("2. Listar contactos")
        print("3. Buscar contacto")
        print("4. Editar contacto")
        print("5. Eliminar contacto")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            agregar_contacto(nombre, telefono, email)
        elif opcion == "2":
            listar_contactos()
        elif opcion == "3":
            nombre = input("Buscar nombre: ")
            buscar_contacto(nombre)
        elif opcion == "4":
            id = int(input("ID del contacto a editar: "))
            nombre = input("Nuevo nombre: ")
            telefono = input("Nuevo teléfono: ")
            email = input("Nuevo email: ")
            editar_contacto(id, nombre, telefono, email)
        elif opcion == "5":
            id = int(input("ID del contacto a eliminar: "))
            eliminar_contacto(id)
        elif opcion == "6":
            break
        else:
            print("Opción no válida.")

def datos():
       conexion = sqlite3.connect("agenda.db")
       cursor = conexion.cursor()
       cursor.execute("SELECT * FROM contactos")
       contactos = cursor.fetchall()
       
       
       with open('C:/Users/Matins/Desktop/Sqlite_2/agenda.csv', 'w') as agenda:
         escritor = csv.writer(agenda)
         datos = ["id","nombre","email","telefono"]
         escritor.writerow(datos)
       for contacto in contactos:
            escritor.writerow(contacto)

conectar()
menu()
datos()

