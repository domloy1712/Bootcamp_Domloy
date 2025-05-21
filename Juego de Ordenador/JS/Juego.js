let palabras= ['vinilo','hombre','viajar','trabajo']
let palabrasecreta = palabras[Math.floor(Math.random()*palabras.length)];
let numfallos = palabrasecreta.length/4;
let fallos = 0;
let intentos = 0;
let palabra_adivinar = [];
let letras_descubiertas = [];

function rallas(palabra){
    palabra_adivinar = [];
   for (let i = 0; i < palabra.length; i++ ){
     palabra_adivinar.push('_');
   }
   document.querySelector('#resultado h1').textContent = palabra_adivinar.join('')
}

let botones = document.getElementById('botones')
botones.addEventListener('click',function(){
    botones.textContent 


})








