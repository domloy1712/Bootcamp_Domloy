var temporal = 0;
var operacion = '';
var entradaCalculadora = document.getElementById('inputID');

function add(num) {
  if (num == 0) {
    if (entradaCalculadora.value[entradaCalculadora.value.length - 1] != '0' || entradaCalculadora.value.length > 1) {
      entradaCalculadora.value = entradaCalculadora.value + num;
    }


  } else if (num == '.') {
    if (entradaCalculadora.value[entradaCalculadora.value.length - 1] != '.' &&
     entradaCalculadora.value != '') {
      entradaCalculadora.value = entradaCalculadora.value + num;
    }
  } else {
    entradaCalculadora.value = entradaCalculadora.value + num;
  }
}

function operacionFunction(operador) {
  operacion = operador;
  temporal = entradaCalculadora.value;
  entradaCalculadora.value = '';
}

    function igual() {
      if (operacion != '') {           
        entradaCalculadora.value = eval(temporal + operacion + entradaCalculadora.value);
      }
    }

function inverso() {
  entradaCalculadora.value = entradaCalculadora.value * -1;
}

function porciento() {
  entradaCalculadora.value = entradaCalculadora.value / 100;
}

function cuadrado() {
  entradaCalculadora.value = entradaCalculadora.value ** 2;
}

function cubo() {
  entradaCalculadora.value = entradaCalculadora.value ** 3;
}

function raiz() {
  entradaCalculadora.value = entradaCalculadora.value ** 0.5;
}

function pi() {
  entradaCalculadora.value = 3.14596;
}

function cleanInput() {
  if (entradaCalculadora.value != '') {
    entradaCalculadora.value = '';
  } else {
    temporal = 0;
    operacion = '';
  }
}




