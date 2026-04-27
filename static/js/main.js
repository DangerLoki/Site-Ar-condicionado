// Toggle mobile menu
function toggleMenu() {
    const menu = document.getElementById("mobileMenu");
    menu.classList.toggle("open");
}

// Navbar shadow on scroll
window.addEventListener("scroll", () => {
    const navbar = document.querySelector(".navbar");
    if (window.scrollY > 10) {
        navbar.style.boxShadow = "0 2px 20px rgba(0,0,0,0.12)";
    } else {
        navbar.style.boxShadow = "0 2px 12px rgba(0,0,0,0.07)";
    }
});

// Smooth reveal on scroll
const observer = new IntersectionObserver(
    (entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
            }
        });
    },
    { threshold: 0.1 }
);

document.querySelectorAll(".service-card, .stat-card, .testimonial-card").forEach((el) => {
    el.style.opacity = "0";
    el.style.transform = "translateY(20px)";
    el.style.transition = "opacity 0.5s ease, transform 0.5s ease";
    observer.observe(el);
});

// CSS class for visible
const style = document.createElement("style");
style.textContent = ".visible { opacity: 1 !important; transform: translateY(0) !important; }";
document.head.appendChild(style);

// Close mobile menu on outside click
document.addEventListener("click", (e) => {
    const menu = document.getElementById("mobileMenu");
    const toggle = document.querySelector(".navbar__toggle");
    if (menu.classList.contains("open") && !menu.contains(e.target) && e.target !== toggle) {
        menu.classList.remove("open");
    }
});
