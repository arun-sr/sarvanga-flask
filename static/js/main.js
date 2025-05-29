var swiper = new Swiper(".newsSwiper", {
    slidesPerView: 1,
    spaceBetween: 10,
    loop: true,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    autoplay: {
        delay: 5000,
    },
    breakpoints: {
        768: {
            slidesPerView: 3,
            spaceBetween: 30,
        },
    },
});


var testimonialsSwiper = new Swiper('.testimonialsSwiper', {
    loop: true,
    pagination: {
        el: '.testimonialsSwiper .swiper-pagination',
        clickable: true,
    },
    autoplay: {
        delay: 5000,
    },
    slidesPerView: 1,
    spaceBetween: 30,
});


new Swiper(".banner-swiper", {
loop: true,
effect: "fade",
autoplay: {
    delay: 5000,
    disableOnInteraction: false
},
navigation: {
    nextEl: "#banner-section-four__swiper-button-next",
    prevEl: "#banner-section-four__swiper-button-prev",
}
});


document.addEventListener("DOMContentLoaded", function () {
const menuToggler = document.querySelector(".side-menu__toggler");
const menuBlock = document.querySelector(".side-menu__block");
const closeBtn = document.querySelector(".side-menu__close-btn");

if (menuToggler) {
    menuToggler.addEventListener("click", function (e) {
        e.preventDefault();
        menuBlock.classList.add("active");
    });
}

if (closeBtn) {
    closeBtn.addEventListener("click", function (e) {
        e.preventDefault();
        menuBlock.classList.remove("active");
    });
}
});

document.addEventListener("DOMContentLoaded", function () {
const dropdownButtons = document.querySelectorAll(".dropdown-btn");

dropdownButtons.forEach(function (btn) {
btn.addEventListener("click", function (e) {
    const parentLi = this.closest("li");
    const submenu = parentLi.querySelector("ul");

    if (submenu) {
        submenu.classList.toggle("open");
        // Optional: toggle arrow direction
        const icon = this.querySelector("span");
        icon.classList.toggle("fa-angle-right");
        icon.classList.toggle("fa-angle-down");
    }
});
});
});