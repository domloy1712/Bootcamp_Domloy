## Ejercicio 1

class Productos:
    def __init__(self,nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def descripcion(self):
      return {f'Este es el {self.nombre} y el {self.precio}'}


class Electronica(Productos):
    def __init__(self,garantia):
        self.garantia = garantia
    
    def info_electronico(self):
       return {f'Info de Electronica{self.nombre}Precio: {self.precio} Garantia: {self.garantia}'}


class Ropa(Productos,Electronica):
    def __init__(self,talla):
        self.talla = talla
    
    def info_ropa(self):
        return{f'Info:{self.nombre}Precio:{self.precio}Talla:{self.talla}'}
    
r = Ropa()
e = Electronica()


print(r)

## Ejercicio 2

class empleado:
    def __init__(self,nombre,salario_base):
        self.nombre = nombre
        self.salario = salario_base
    
    def calcular_salario(self):
       return self.salario

class gerente(empleado):
    def __init__(self,bonificacion):
      self.bonificacion = bonificacion
    
    def calcular_salario(self):
        return self.bonificacion + self.salario 
       

class operario(empleado):
    def __init__(self,oras_extras):
        self.oras = oras_extras
    
    def calcular_salario(self):
        return self.oras + self.salario


o = operario.calcular_salario()
g = gerente.calcular_salario()

## Ejercicio 3

class persona:
    def __init__(self,nombre,edad):
       self.nombre = nombre
       self.edad = edad
    
    def rol(self):
      print('Esta persona tiene un rol en la Escuela')

class estudiante(persona):
    def __init__(self,grado):
      self.grado = grado
    
    def rol(self):
      print(f'Soy estudiante del grado: {self.grado}')

class professor(persona):
   def __init__(self,materia):
      self.materia = materia
   def rol(self):
      print(f'Soy professor de la materia: {self.materia}')

class director(persona):
  