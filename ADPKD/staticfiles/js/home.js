document.addEventListener("DOMContentLoaded", function () {
    let loader = document.getElementById("preloader");
    loader.style.display = 'none';

    let sliderWrapper = document.querySelector(".slider-wrapper");
    let items = document.querySelectorAll(".items");

    items.forEach(item => {
        let clone = item.cloneNode(true);
        sliderWrapper.appendChild(clone);
    });

    let totalWidth = sliderWrapper.scrollWidth / 2;
    let duration = totalWidth / 50;
    sliderWrapper.style.animationDuration = duration + "s";
});