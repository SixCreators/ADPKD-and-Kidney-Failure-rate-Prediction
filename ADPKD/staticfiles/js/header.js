let m_icon = document.querySelector(".menu_bar");
let nav_btn = document.querySelector(".navbar");
let header_btn = document.querySelector(".header_btn");

/* this section for click menu bar show nev bar section */
m_icon.addEventListener("click", () => {
    nav_btn.classList.toggle("shownav_bar");
});

/* this section for click menu bar show header button(login, sign up) section */
m_icon.addEventListener("click", () => {
    header_btn.classList.toggle("showheader_btn");
});


/* this section for menu bar class add */
let menu_container = document.querySelector(".menu-container");

menu_container.addEventListener("click", () => {
    menu_container.classList.toggle("active");
});