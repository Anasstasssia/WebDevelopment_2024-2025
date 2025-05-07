document.addEventListener("DOMContentLoaded", function () {

    // === АВТО-ПРОКРУТКА ГАЛЕРЕИ ===
    const galleryScroll = document.querySelector(".gallery-scroll");

    // Клонируем всё содержимое галереи
    const galleryContent = galleryScroll.innerHTML;
    galleryScroll.innerHTML += galleryContent;

    let scrollSpeed = 0.5; // скорость прокрутки
    let scrollPosition = 0;
    let isPaused = false;

    function animateScroll() {
        if (!isPaused) {
            scrollPosition += scrollSpeed;
            if (scrollPosition >= galleryScroll.scrollWidth / 2) {
                scrollPosition = 0;
            }
            galleryScroll.scrollLeft = scrollPosition;
        }
        requestAnimationFrame(animateScroll);
    }

    animateScroll();

    // Остановить при взаимодействии
    ["mouseenter", "touchstart", "mousedown"].forEach(event => {
        galleryScroll.addEventListener(event, () => {
            isPaused = true;
        });
    });

    ["mouseleave", "touchend", "mouseup"].forEach(event => {
        galleryScroll.addEventListener(event, () => {
            isPaused = false;
        });
    });

    

    // === АУДИО ===
    const imageElements = document.querySelectorAll("img[id^='image-']");
    imageElements.forEach(img => {
        const idSuffix = img.id.replace('image-', '');
        const audio = document.getElementById(`memeAudio_${idSuffix}`);
        if (audio) {
            img.addEventListener("click", () => {
                if (audio.paused) {
                    audio.play();
                } else {
                    audio.pause();
                    audio.currentTime = 0;
                }
            });
        }
    });

    // === ПЕРЕХОД К ИЗОБРАЖЕНИЮ ===
    const galleryImages = document.querySelectorAll(".gallery-item img");
    galleryImages.forEach(item => {
        item.addEventListener("click", () => {
            const name = item.getAttribute("data-name");
            const target = document.getElementById(`image-${name}`);
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'center' });
                target.classList.add('highlight');
                setTimeout(() => target.classList.remove('highlight'), 1500);
            }
        });
    });

    

    // === КОЛЛАПС ===
    window.toggleCollapsible = function (elem) {
        const content = elem.nextElementSibling;
        content.style.display = (content.style.display === "block") ? "none" : "block";
    };

    


});
