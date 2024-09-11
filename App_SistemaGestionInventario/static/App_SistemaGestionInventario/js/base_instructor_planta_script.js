const boton_ventana_registrar_material = document.getElementById("contenedor-botones-registrar");
const ventana_registrar_material = document.getElementById("botones-registrar");



boton_ventana_registrar_material.addEventListener("click", () => {
    console.log("WENITAS aaaaaaaaaaaaaaaaaaaa")
    ventana_registrar_material.style.display = "block";
});

window.addEventListener("click", (event) => {
    if (event.target === ventana_registrar_material) {
        console.log("WENITAS ayudaaaaaaaaaaaaaaaaaa")
        ventana_registrar_material.style.display = "none";
    }
  });