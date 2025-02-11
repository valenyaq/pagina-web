document.addEventListener("DOMContentLoaded", function () {
    const submenuBtn = document.querySelector(".submenu-btn");
    const submenuList = document.querySelector(".submenu-list");

    // Abrir o cerrar el submenú al hacer clic en el botón
    submenuBtn.addEventListener("click", function (event) {
        event.stopPropagation(); // Evitar que el clic se propague al documento
        submenuList.classList.toggle("visible");
    });

    // Cerrar el submenú si se hace clic fuera de él
    document.addEventListener("click", function (event) {
        // Verificar si el clic se realizó fuera del submenú y del botón
        if (!submenuList.contains(event.target) && !submenuBtn.contains(event.target)) {
            submenuList.classList.remove("visible");
        }
    });
});
