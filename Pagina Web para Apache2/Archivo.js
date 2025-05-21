function actualizarReloj(){
    
    const ahora = new Date();
    let horas = ahora.getHours();
    let minutos = ahora.getMinutes();
    let seconds = ahora.getSeconds();

    horas = horas < 10?'0'+horas:horas;
    minutos = minutos < 10? '0'+minutos:minutos;
    seconds = seconds < 10? '0'+seconds:seconds;

    document.getElementById('reloj').textContent=`${horas}:${minutos}:${seconds}`

    const horaMeta = new Date();
    horaMeta.setHours(14, 0, 0, 0);
    const diferencia = horaMeta - ahora;
    
     if (diferencia > 0) {
    let horasRestantes = Math.floor(diferencia / 1000 / 60 / 60);
    let minutosRestantes = Math.floor((diferencia % (1000 * 60 * 60)) / (1000 * 60));
    let segundosRestantes = Math.floor((diferencia % (1000 * 60)) / 1000);

    horasRestantes = horasRestantes < 10? '0'+ horasRestantes:horasRestantes;
    minutosRestantes = minutosRestantes <10? '0'+ minutosRestantes:minutosRestantes;
    segundosRestantes = segundosRestantes <10? '0'+ segundosRestantes:segundosRestantes;

    document.getElementById('contador').textContent=`${horasRestantes}:${minutosRestantes}:${segundosRestantes}`
 } else {
    alert('¡Ya es, la Hora de irse a Casa!');
}
}
setInterval(actualizarReloj,1000);
actualizarReloj()
