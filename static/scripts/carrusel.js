document.addEventListener("DOMContentLoaded", function () {
    const track = document.querySelector(".carrusel-track");
    const slides = Array.from(document.querySelectorAll(".carrusel-slide"));
    const prevButton = document.querySelector(".prev-btn");
    const nextButton = document.querySelector(".next-btn");

    const slideWidth = slides[0].getBoundingClientRect().width; // Ancho de cada diapositiva
    let currentIndex = 0;

    // Mover el carrusel
    const moveToSlide = (index) => {
        track.style.transform = `translateX(-${slideWidth * index}px)`;
        currentIndex = index;
    };

    // Botón siguiente
    nextButton.addEventListener("click", () => {
        if (currentIndex < slides.length - 4) {
            moveToSlide(currentIndex + 1);
        }
    });

    // Botón anterior
    prevButton.addEventListener("click", () => {
        if (currentIndex > 0) {
            moveToSlide(currentIndex - 1);
        }
    });
});
