function esBisiesto(anio) {
    return (anio % 4 === 0 && anio % 100 !== 0) || (anio % 400 === 0);
}

function generarCalendario() {
    const inputFecha = document.getElementById("fecha");
    const fecha = inputFecha.value;
    const parts = fecha.split('-');
    const anio = parseInt(parts[0]);
    const mes = parseInt(parts[1]) - 1; // Restar 1 al mes porque en JavaScript los meses van de 0 a 11
    const contenedorCalendario = document.getElementById("contenedorCalendario");
    let diasEnMes = [31, esBisiesto(anio) ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

    let calendarioHTML = "<table>";
    calendarioHTML += "<tr><th colspan='7'>" + (mes + 1) + "/" + anio + "</th></tr>";
    calendarioHTML += "<tr><th>Lun</th><th>Mar</th><th>Mié</th><th>Jue</th><th>Vie</th><th>Sáb</th><th>Dom</th></tr>";
    calendarioHTML += "<tr>";
    let dia = 1;
    let diaSemanaActual = new Date(anio, mes, 1).getDay();
    diaSemanaActual = diaSemanaActual === 0 ? 6 : diaSemanaActual - 1; // Convertir el domingo (0) en 6 (sábado)

    // Llenar días vacíos antes del primer día del mes
    for (let i = 0; i < diaSemanaActual; i++) {
        calendarioHTML += "<td></td>";
    }

    while (dia <= diasEnMes[mes]) {
        if (diaSemanaActual === 7) {
            calendarioHTML += "</tr><tr>";
            diaSemanaActual = 0;
        }

        calendarioHTML += `<td><a href="#${anio}-${mes + 1}-${dia}">${dia}</a></td>`;
        diaSemanaActual++;
        dia++;
    }

    // Completar la última fila con celdas vacías si es necesario
    while (diaSemanaActual < 7) {
        calendarioHTML += "<td></td>";
        diaSemanaActual++;
    }

    calendarioHTML += "</tr>";
    calendarioHTML += "</table>";

    contenedorCalendario.innerHTML = calendarioHTML;
}

// Generar el calendario cuando se cargue la página por primera vez
generarCalendario();