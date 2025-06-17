// Detecção automática de tema
function updateTheme() {
    const prefersDark = window.matchMedia(
        "(prefers-color-scheme: dark"
    ).matches;
    document.documentElement.setAttribute(
        "data-bs-theme",
        prefersDark ? "dark" : "light"
    );
}

// Inicialização
document.addEventListener("DOMContentLoaded", function () {
    updateTheme();
    updateDynamicCard();

    // Monitora mudanças de tema
    window
        .matchMedia("(prefers-color-scheme: dark)")
        .addEventListener("change", updateTheme);
});