document.addEventListener("DOMContentLoaded", function () {
    const navLinks = document.querySelectorAll(".nav-links a");
    const sections = document.querySelectorAll(".section");

    // Show the "About" section by default
    document.querySelector("#about").classList.add("active");

    // Add click event listeners to navigation links
    navLinks.forEach(link => {
        link.addEventListener("click", event => {
            event.preventDefault();

            // Remove "active" class from all sections
            sections.forEach(section => section.classList.remove("active"));

            // Add "active" class to the clicked section
            const targetId = link.getAttribute("href").substring(1);
            document.getElementById(targetId).classList.add("active");
        });
    });
});
