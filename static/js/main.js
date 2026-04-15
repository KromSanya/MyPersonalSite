document.addEventListener("DOMContentLoaded", function () {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll(".nav-link");

    navLinks.forEach(link => {
        const linkPath = new URL(link.href).pathname;

        if (linkPath === currentPath) {
            link.classList.add("active");
            link.setAttribute("aria-current", "page");
        }
    });

    const animatedBlocks = document.querySelectorAll(
        ".card, .hero-box, .not-found-box, .hero-section, .hero-side-card"
    );

    animatedBlocks.forEach((block, index) => {
        block.classList.add("fade-in");
        block.style.animationDelay = `${index * 0.12}s`;
    });
});