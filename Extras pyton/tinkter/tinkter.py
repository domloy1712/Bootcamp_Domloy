import tkinter as tk


ventana = tk.Tk()

# Configuración de la ventana
ventana.title("Mi primera ventana")
ventana.geometry("100x100")
tk.Label(ventana, text="ola").pack()
# Crear un botón
def saludar():
    tk.Label(ventana, text="Hola, mundo!").pack()

tk.Button(ventana, text="Saludar", command=saludar).pack()
ventana.mainloop()

