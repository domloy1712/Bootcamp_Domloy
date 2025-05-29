Usuario = input("Introduzca su usuario")
Año_de_Nacimiento = int(input("Introduzca su año de nacimiento"))
Residencia = input("Donde vive?")
mascota = input("Tienes Mascota? si/no")
Edad = 2025 - Año_de_Nacimiento
Color = input("Dame un color")


if (mascota == "si"):
    print ("Muy bien")
else:
    print("Muy mal estaras solo en la vida pringado")


if ( Edad < 18 ):
    print ("Es menor de edad")
elif ( Edad > 18 ):
    print ("Es un adulto")
elif ( Edad > 60 ): 
    print ("Es un viejales")



print("Tu usuario", Usuario)
print( "Tu año de nacimiento es:", Año_de_Nacimiento)
print("Años:", Edad)
print("vive en:", Residencia)
print("su color", Color)