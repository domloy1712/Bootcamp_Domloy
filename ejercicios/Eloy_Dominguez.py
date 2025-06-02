Usuario = input("Introduzca su usuario")
Año_de_Nacimiento = int(input("Introduzca su año de nacimiento"))
Residencia = input("Donde vive?")
mascota = input("Tienes Mascota? si/no")
Edad = 2025 - Año_de_Nacimiento
Color = input("Dame un color")

print("Tu usuario", Usuario)
print( "Tu año de nacimiento es:", Año_de_Nacimiento)
print("vive en:", Residencia)

if (mascota == "si"):
    print ("Muy bien")
else:
    print("Muy mal estaras solo en la vida pringado")

print("Años:", Edad)

if ( Edad < 18 ):
    print ("Es menor de edad")
elif ( Edad > 18 ):
    print ("Es un adulto")
elif ( Edad > 60 ): 
    print ("Es un viejales")

print("su color", Color)