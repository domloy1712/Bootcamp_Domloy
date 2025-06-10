import os

directorio = "/ruta/a/tu/carpeta/de/archivos"  
prefijo = "notas_"

for arcivos in os.listdir(directorio):
        ruta_antigua = os.path.join(directorio, arcivos)
        
        if os.path.isfile(ruta_antigua):
        
         nuevo = prefijo + arcivos
         ruta_nueva = os.path.join(directorio, nuevo)
         os.rename(ruta_antigua, ruta_nueva)
print(f"Renombrado: {arcivos} -> {nuevo}")

