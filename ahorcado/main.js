let palabras = ['forquilla', 'ganivet', 'pepit', 'carrusel', 'muntanya', 'porta', 'edifici', 'pixapins', 'amenaça', 'aixeta', 'arxipielag', 'grunxador', 'finestra', 'xerraire'];
let palabra_secreta = palabras[Math.floor(Math.random() * palabras.length)];
let num_fallos = palabra_secreta.length/2; // Número máximo de fallos permitidos
let fallos = 0;
let intentos = 0;
let palabra_adivinada = [];
let letras_adivinadas = [];

function asterisquear(palabra) {
    palabra_adivinada = [];
    for (let i = 0; i < palabra.length; i++) {
        palabra_adivinada.push('*');
    }
    document.querySelector('#resultado h2').textContent = palabra_adivinada.join(' ');
}

function mostrarResultado() {
    document.getElementById('num_fallos').textContent = 'Nº Fallos: ' + fallos+` - Max. ${Math.floor(num_fallos)}`;
    document.getElementById('num_intentos').textContent = 'Nº Intentos: ' + intentos;

    if (fallos >= num_fallos) {
        alert('Has perdido! La palabra era: ' + palabra_secreta);
        location.reload();
    }

    if (palabra_adivinada.join('') === palabra_secreta) {
        alert('¡Has ganado!');
        location.reload();
    }
}

function actualizarPalabra(letra) {
    for (let i = 0; i < palabra_secreta.length; i++) {
        if (palabra_secreta[i] === letra) {
            palabra_adivinada[i] = letra;
        }
    }
    document.querySelector('#resultado h2').textContent = palabra_adivinada.join(' ');
}

document.getElementById('boton').addEventListener('click', function (e) {
    e.preventDefault();
    let letra = document.getElementById('input').value.toLowerCase();

    if (letra && !letras_adivinadas.includes(letra)) {
        letras_adivinadas.push(letra);
        intentos++;

        if (palabra_secreta.includes(letra)) {
            actualizarPalabra(letra);
        } else {
            fallos++;
        }

        mostrarResultado();
    }

    document.getElementById('input').value = ''; // Limpiar input
    document.getElementById('input').focus(); // Mantener foco en el input
});

asterisquear(palabra_secreta);
