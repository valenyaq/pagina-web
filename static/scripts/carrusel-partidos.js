document.addEventListener("DOMContentLoaded", function () {
    const prevButtonPartidos = document.querySelector(".prev-btn");
    const nextButtonPartidos = document.querySelector(".next-btn");
    const trackPartidos = document.querySelector(".proximos-partidos");
    const partidos = Array.from(document.querySelectorAll(".partido"));

    const partidoWidth = partidos[0].getBoundingClientRect().width; // Ancho de cada partido
    let currentIndexPartidos = 0;

    // Mover el carrusel
    const moveToSlidePartidos = (index) => {
        trackPartidos.style.transform = `translateX(-${partidoWidth * index}px)`;
        currentIndexPartidos = index;
    };

    // Botón siguiente
    nextButtonPartidos.addEventListener("click", () => {
        if (currentIndexPartidos < partidos.length - 3) { // Si hay más de 3 partidos, avanza
            moveToSlidePartidos(currentIndexPartidos + 1);
        }
    });

    // Botón anterior
    prevButtonPartidos.addEventListener("click", () => {
        if (currentIndexPartidos > 0) { // Si no está en el primer partido, retrocede
            moveToSlidePartidos(currentIndexPartidos - 1);
        }
    });
});
