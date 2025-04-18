document.addEventListener("DOMContentLoaded", function () {
    let scrollPosition = 0;

    document.querySelector(".header__hamburger").addEventListener("click", function () {
        this.classList.toggle("active");
        const burgerButton = document.querySelector(".header__hamburger");
        const mobileMenu = document.querySelector(".header__mobile-menu");
        const body = document.querySelector("body");

        mobileMenu.classList.toggle('active');

        if (mobileMenu.classList.contains('active')) {
            burgerButton.querySelector('img').src = '/static/images/close-burger.svg';
        } else {
            burgerButton.querySelector('img').src = '/static/images/burger-icon.svg';
        }

        if (mobileMenu.classList.contains("active")) {
            // Сохраняем текущую позицию и отключаем прокрутку
            scrollPosition = window.scrollY;
            body.classList.add("scroll-disabled");
            body.style.top = `-${scrollPosition}px`;
        } else {
            // Убираем блокировку и восстанавливаем позицию
            body.classList.remove("scroll-disabled");
            body.style.top = "";
            window.scrollTo(0, scrollPosition);
        }
    });
});