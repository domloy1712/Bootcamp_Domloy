import sqlite3

def conectar():
    conexion = sqlite3.connect("patos.db")
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS patos(" 
    "id_patos INTEGER PRIMARY KEY AUTOINCREMENT," 
    "nombre TEXT);")
    cursor.execute("CREATE TABLE IF NOT EXISTS articulos(" 
    "id_articulos INTEGER PRIMARY KEY AUTOINCREMENT," 
    "nombre TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS outfit(" 
    "id_articulos INTEGER," 
    "id_patos INTEGER," 
    "FOREIGN KEY (id_patos) REFERENCES patos(id_patos)," 
    "FOREIGN KEY (id_articulos) REFERENCES articulos(id_articulos))")
    conexion.commit()
    conexion.close()

def agregar_patos(nombre):
    conexion = sqlite3.connect("patos.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO patos (nombre) VALUES (?)", (nombre,))
    conexion.commit()
    conexion.close()

def agregar_articulos(nombre):
    conexion = sqlite3.connect("patos.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO articulos (nombre) VALUES (?)", (nombre,))
    conexion.commit()
    conexion.close()

def añadir_outfits(id_patos, id_articulos):
   conexion = sqlite3.connect("patos.db")
   cursor = conexion.cursor()
   cursor.execute("INSERT INTO outfit (id_patos,id_articulos) VALUES (?,?)", (id_patos, id_articulos))
   conexion.commit()
   conexion.close()


def listar_patos():
    conexion = sqlite3.connect("patos.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM patos")
    patos = cursor.fetchall()
    conexion.close()

    for pato in patos:
        print(f"ID: {pato[0]}, Nombre: {pato[1]}")

def listar_articulos():
    conexion = sqlite3.connect("patos.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM articulos")
    articulos = cursor.fetchall()
    conexion.close()

    for articulo in articulos:
        print(f"id: {articulo[0]}, nombre: {articulo[1]}")

def listar_patos_con_sus_articulos():
    conexion = sqlite3.connect("patos.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT p.nombre, a.nombre " 
    "FROM Outfit o" 
    "JOIN articulos a" 
    "ON o.id_articulos=a.id_articulos" 
    "JOIN patos p" 
    "ON o.id_patos=p.id_patos")
    patos = cursor.fetchall()
    conexion.close()

    for pato in patos:
        print(f"nombre: {pato[0]}, articulo: {pato[1]}")

def modificar_pato(id,nombre):
     conexion = sqlite3.connect("patos.db")
     cursor = conexion.cursor()
     cursor.execute("UPDATE patos SET nombre=? WHERE id_patos = ?",(nombre,id))
     conexion.commit()
     conexion.close()

def modificar_articulo(id,nombre):
     conexion = sqlite3.connect("patos.db")
     cursor = conexion.cursor()
     cursor.execute("UPDATE articulo SET nombre=? WHERE id_articulos = ?",(nombre,id))
     conexion.commit()
     conexion.close()

def eliminar_patos(id):
    conexion = sqlite3.connect("agenda.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM patos WHERE id_patos = ?", (id))
    conexion.commit()
    conexion.close()

def eliminar_articulos(id):
    conexion = sqlite3.connect("patos.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM articulos WHERE id_articulos = ?", (id))
    conexion.commit()
    conexion.close()

def menu():
     while True:
          intro = input("Te gustan los Patitos? (SI|NO):")
        
          if intro == "NO":
              print("Muy mal a todos te tienen que gustar los patitos")
          elif intro == "SI":
              print("Ue!!!! Respuesta correcta, Que quieres hacer?")
            
            
              while True:
                 
               print("\n1.Que patitos hay?")
               print("2.Que ropa hay?")
               print("3.Quiero ver el outfit de un patito")
               print("4.QUIERO ASESINAR A PATITOS!!!")
               print("5.Quiero elimnar ropa")
               print("6.Quiero modificar ropa")
               print("7.Quiero cambiar el nombre Patitos")
               print("8.SI MAS PATITOS UE!!!!!")
               print("9.Quiero poner mas ropa, que queda poca")
               print("10.Quiero crear Outfits")
              
               opcion = int(input("Que quieres hacer?"))
              
               if opcion == 1:
                 listar_patos() 
               elif opcion == 2:
                  listar_articulos()
               elif opcion == 3:
                   listar_patos_con_sus_articulos()
               elif opcion == 4 :
                    id = int(input("Dime el numero de que patito asesinar UAJAJAJAJA!!!!: "))
                    eliminar_patos(id)
               elif opcion == 5 :
                   id = int(input("Quiero borra ropa, porque tengo mucha ropa: "))
                   eliminar_articulos(id)
               elif opcion == 6:
                  id = int(input("Articulo a modificar: "))
                  nombre = input("Nombre del Articulo: ")
                  modificar_articulo(id, nombre)
               elif opcion == 7:
                  id = int(input("Patito a modificar:"))
                  nombre = input("Nuevo nombre:")
                  modificar_pato(id)
               elif opcion == 8:
                  nombre = input("Nombre: ")
                  agregar_patos(nombre)
               elif opcion == 9: 
                   nombre = input("Nombre")
                   agregar_articulos(nombre)
               elif opcion == 10:
                   print ("Que outfit quieres añadir?")
                   id_articulos = int(input("Id de la ropa"))
                   id_patos = int(input("Id del pato \n"))
                   añadir_outfits(id_patos, id_articulos)
               else:
                   print("Muy bien,no has hecho nada a mis patito, largate deja en paz a mis patitos!!!! USURPADOR!!!!!")

conectar()
menu()


                   
                  

               