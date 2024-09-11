const boton_ventana_opcion_material = document.getElementById("contenedor-botones-suministro");
const ventana_opcion_material = document.getElementById("botones-suministro");

boton_ventana_opcion_material.addEventListener("click", () => {
    ventana_opcion_material.style.display = "block";
});

window.addEventListener("click", (event) => {
    if (event.target === ventana_opcion_material) {
        ventana_opcion_material.style.display = "none";
    }
  });