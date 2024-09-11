/**
 * Función para alternar la visibilidad del menú desplegable
 */
function toggleMenu() {
    // Obtén la referencia al elemento del menú desplegable
    var dropdownMenu = document.getElementById("myDropdown");

    // Verifica si el menú está oculto o visible y alterna su estado
    if (dropdownMenu.style.display === "none" || dropdownMenu.style.display === "") {
        dropdownMenu.style.display = "block"; // Muestra el menú
    } else {
        dropdownMenu.style.display = "none"; // Oculta el menú
    }
}

/**
 * Manejador de clics en la ventana para cerrar el menú cuando se hace clic fuera de él
 */
window.onclick = function (event) {
    // Verifica si el clic no está en el elemento de activación del menú
    if (!event.target.matches('.menu-trigger')) {
        // Obtiene todos los elementos de menú desplegable
        var dropdowns = document.getElementsByClassName("dropdown-menu");

        // Itera sobre los elementos y cierra aquellos que están abiertos
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.style.display === "block") {
                openDropdown.style.display = "none"; // Oculta el menú
            }
        }
    }
}