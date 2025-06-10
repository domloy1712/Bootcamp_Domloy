import mysql.connector

class AgendaMySQL:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="agenda"
        )
        self.cursor = self.conn.cursor()

    def menu(self):
        while True:
            print("\n------ Agenda Personal ------")
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            opcion = input("Introduzca la opción deseada: ")

            if opcion == "1":
                self.anadir()
            elif opcion == "2":
                self.lista()
            elif opcion == "3":
                self.buscar()
            elif opcion == "4":
                self.editar()
            elif opcion == "5":
                print("Saliendo de la agenda ...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def anadir(self):
        print("\n--- Añadir nuevo contacto ---")
        nom = input("Introduzca el nombre: ")
        telf = input("Introduzca el teléfono: ")
        email = input("Introduzca el email: ")
        sql = 'INSERT INTO Contactos(nombre,telefono,email) VALUES ( %s, %s, %s)'
        self.cursor.execute(sql,(nom,telf,email))
        self.conn.commit()
        print("Contacto añadido correctamente.")



    def lista(self):
        print("\n--- Lista de contactos ---")
        self.cursor.execute('SELECT * FROM contactos')
        contactos = self.cursor.fetchall()
        if not contactos:
            print("No hay ningún contacto en la agenda.")
        else:
            for i, contacto in enumerate(contactos, 1):
                print(f"{i}. {contacto[1]}, {contacto[2]}, {contacto[3]}")

    def buscar(self):
        print("\n--- Buscador de contactos ---")
        nom = input("Introduzca el nombre del contacto: ")
        self.cursor.execute('SELECT * FROM contactos WHERE nombre LIKE %s',(f"%{nom}%",))
        resultados = self.cursor.fetchall()
        if resultados:
            for r in resultados:
                print("Datos del Contacto")
                print(f"Nombre:", r['nombre'])
                print(f"Telefono:", r['telefono'])
                print(f"Email:", r['email'])
        else:
            print('Contacto no encontrado')
             

    def editar(self):
        print("\n--- Editar contacto ---")
        id_contacto = self.buscar()
        if id_contacto is not None:
            while True:
                print("\n¿Qué desea editar?")
                print("1. Nombre")
                print("2. Teléfono")
                print("3. Email")
                print("4. Volver")
                opcion = input("Introduzca la opción deseada: ")

                if opcion == "1":
                    nuevo_nombre = input("Nuevo nombre: ")
                    self.cursor.execute('UPDATE contactos SET nombre=%s WHERE id = %s',(nuevo_nombre,id_contacto))
                elif opcion == "2":
                    nuevo_telf = input("Nuevo teléfono: ")
                    self.cursor.excute('UPDATE contactos SET telefono=%s WHERE id = %s',(nuevo_telf,id_contacto))
                elif opcion == "3":
                    nuevo_email = input("Nuevo email: ")
                    self.cursor.excute('UPDATE contactos SET email=%s WHERE id = %s',(nuevo_email,id_contacto))
                elif opcion == "4":
                    print("Volviendo al menú principal...")
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")
        else:
            print("No se puede editar un contacto no encontrado.")



agenda = AgendaMySQL()
agenda.menu()
