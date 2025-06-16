import sqlite3
from datetime import datetime
from models import Pelicula, Cliente, Alquiler
import csv

class DBManager:
    def __init__(self, db_name="videoclub.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS peliculas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT,
                disponible INTEGER DEFAULT 1        
         )""")
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT
            )""")
        
        self.cursor.execute("""
            
            CREATE TABLE IF NOT EXISTS alquileres (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente_id INTEGER,
                pelicula_id INTEGER,
                fecha TEXT,
                fecha_vencimiento TEXT,
                penalizacion INT,
                devuelto INTEGER DEFAULT 0          
            )""")
        
        self.conn.commit()

    def agregar_pelicula(self, titulo):
        self.cursor.execute("INSERT INTO peliculas (titulo) VALUES (?)", (titulo,))
        self.conn.commit()

    def listar_peliculas(self):
        self.cursor.execute("SELECT * FROM peliculas")
        return [Pelicula(*row) for row in self.cursor.fetchall()]
    
    def registrar_cliente(self, nombre):
        self.cursor.execute("INSERT INTO clientes (nombre) VALUES (?)", (nombre,))
        self.conn.commit()

    def listar_clientes(self):
        self.cursor.execute("SELECT * FROM clientes")
        return [Cliente(*row) for row in self.cursor.fetchall()]
    
    def alquilar_pelicula(self, cliente_id, pelicula_id):
        self.cursor.execute("SELECT disponible FROM peliculas WHERE id=?",(pelicula_id,))
        if self.cursor.fetchone()[0] == 0:
            return False
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
        fecha_vencimiento = datetime.now() 
        self.cursor.execute("INSERT INTO alquileres (cliente_id, pelicula_id, fecha, fecha_vencimiento) VALUES (?,?,?,?)",
                            (cliente_id, pelicula_id, fecha, fecha_vencimiento))
        self.cursor.execute("UPDATE peliculas SET disponible=0 where id=?",(pelicula_id,))
        self.conn.commit()
    
    def devolver_pelicula(self, pelicula_id):
        self.cursor.execute("UPDATE peliculas SET disponible=1 where id=?",(pelicula_id,))
        self.cursor.execute("UPDATE alquileres SET devuelto=1 where id=?",(pelicula_id,))
        self.conn.commit()

    def historial(self):
        self.cursor.execute("""
            SELECT a.id, c.nombre, p.titulo, a.fecha, a.devuelto
            FROM alquileres a
            JOIN clientes c ON a.cliente_id=c.id
            JOIN peliculas p ON a.pelicula_id=p.id
            ORDER BY a.fecha DESC
        """)
        return self.cursor.fetchall()
    
 
    
    
