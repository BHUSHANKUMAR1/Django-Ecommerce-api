// var button = document.getElementById('right');
// button.onclick = function () {
//     var container = document.getElementById('box');
//     sideScroll(container, 'right', 12, 100, 10);
// };

// var back = document.getElementById('left');
// back.onclick = function () {
//     var container = document.getElementById('box');
//     sideScroll(container, 'left', 12, 100, 10);
// };

// function sideScroll(element, direction, speed, distance, step) {
//     scrollAmount = 0;
//     var slideTimer = setInterval(function () {
//         if (direction == 'left') {
//             element.scrollLeft -= step;
//         } else {
//             element.scrollLeft += step;
//         }
//         scrollAmount += step;
//         if (scrollAmount >= distance) {
//             window.clearInterval(slideTimer);
//         }
//     }, speed);
// }


// var swiper = new Swiper(".slide-content", {
//     slidesPerView: 3,
//     spaceBetween: 25,
//     loop: true,
//     centerSlide: 'true',
//     fade: 'true',
//     grabCursor: 'true',
//     pagination: {
//         el: ".swiper-pagination",
//         clickable: true,
//         dynamicBullets: true,
//     },
//     navigation: {
//         nextEl: ".swiper-button-next",
//         prevEl: ".swiper-button-prev",
//     },

//     breakpoints: {
//         0: {
//             slidesPerView: 1,
//         },
//         520: {
//             slidesPerView: 2,
//         },
//         950: {
//             slidesPerView: 3,
//         },
//     },
// });


const prev = document.querySelector('.prev')
const next = document.querySelector('.next')
const slider = document.querySelector('.slider')


prev.addEventListener('click', () => {
    slider.scrollLeft -= 100
})

next.addEventListener('click', () => {
    slider.scrollLeft += 100
})



