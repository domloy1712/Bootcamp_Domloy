Usuario = input("Introduzca su usuario")
Año_de_Nacimiento = int(input("Introduzca su año de nacimiento"))
print("Tu usuario", Usuario)
print( "Tu año de nacimiento es:", Año_de_Nacimiento)
print("Años:", 2025 - Año_de_Nacimiento)
Residencia = input("Donde vive?")
print("vive en:", Residencia)
mascota = input("Tienes Mascota? si/no")
Edad = 2025 - Año_de_Nacimiento

if (mascota == "si"):
    print ("Muy bien")
else:
    print("Muy mal estaras solo en la vida pringado")

Color = input("Dame un color")
print("su color", Color)

if ( Edad < 18 ):
    print ("Es menor de edad")
elif ( Edad > 18 ):
    print ("Es un adulto")
elif ( Edad > 60 ): 
    print ("Es un viejales")




