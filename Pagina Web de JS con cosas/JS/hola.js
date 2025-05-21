let boton = document.getElementById("Cambiar")

boton.onclick = function (){
    ventana = window.open ("", "_blank", "width=600,height=400");
    ventana.document.write ('<h1>Texto Modificado</h1>')
}

