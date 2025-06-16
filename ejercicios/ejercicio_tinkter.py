from abc import ABC, abstractmethod
import mysql.connector

def connectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="empresa"
    )

class Empleado(ABC):
  def __init__(self, nombre, sueldo_base):
   self._nombre = nombre
   self._sueldo_base = sueldo_base



def descripcion(self):
  return f"{self._nombre} - {self.__class__.__name__}"
# Método abstracto (requiere polimorfismo)
@abstractmethod
def calcular_salario_total(self):
  pass


class Programador(Empleado):
 def calcular_salario_total(self):
  return self._sueldo_base + 1000


class Diseñador(Empleado):
 def calcular_salario_total(self):
  return self._sueldo_base * 1.05


class Gerente(Empleado):
 def calcular_salario_total(self):
  return self._sueldo_base * 1.10 + 2000


def mostrar_salario_empleado(empleado):
  print(empleado.descripcion())
  print(f"Salario total: {empleado.calcular_salario_total():.2f} €\n")

def insertar_empleado(nombre,tipo,sueldo_base):
    conexion = connectar()
    cursor = conexion.cursor()
    sql = "INSERT INTO empleados (nombre, tipo, sueldo_base) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nombre, tipo, sueldo_base))
    conexion.commit()
    cursor.close()
    conexion.close()

def listar_empleados():
    conexion = connectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, tipo, sueldo_base FROM empleados")
    empleados = cursor.fetchall()
    cursor.close()
    conexion.close()
    
    for emp in empleados:
        nombre, tipo, sueldo_base = emp
        if tipo == 'Programador':
            empleado = Programador(nombre, sueldo_base)
        elif tipo == 'Diseñador':
            empleado = Diseñador(nombre, sueldo_base)
        elif tipo == 'Gerente':
            empleado = Gerente(nombre, sueldo_base)
        else:
            continue

    print(f"{Empleado.descripcion()} - Salario total: {empleado.calcular_salario_total():.2f} €")