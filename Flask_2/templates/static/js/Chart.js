async function obtenerDatos() {
    const response = await fetch('http://192.168.1.50:5000'); 
    const data = await response.text();
    console.log(data);
}

setInterval(obtenerDatos, 10000); // Cada 10 segundos
