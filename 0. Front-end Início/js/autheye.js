// js/funcionalidadeolho.js

/**
 * Alterna a visibilidade da senha e os ícones
 * @param {HTMLElement} iconElement - Elemento do ícone que foi clicado
 */
function togglePasswordVisibility(iconElement) {
    // Encontra o container pai dos ícones
    const container = iconElement.closest('.eyes-slashnfill');
    // Encontra o input de senha relacionado
    const passwordInput = container.closest('.form-floating').querySelector('input[type="password"], input[type="text"]');
    
    // Alterna o tipo do input
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        // Esconde todos os ícones primeiro
        container.querySelectorAll('i').forEach(icon => icon.style.display = 'none');
        // Mostra o ícone de olho fechado
        container.querySelector('.bi-eye-slash').style.display = 'inline-block';
    } else {
        passwordInput.type = 'password';
        // Esconde todos os ícones primeiro
        container.querySelectorAll('i').forEach(icon => icon.style.display = 'none');
        // Mostra o ícone de olho aberto
        container.querySelector('.bi-eye').style.display = 'inline-block';
    }
}

/**
 * Configura os eventos quando o DOM estiver carregado
 */
document.addEventListener('DOMContentLoaded', function() {
    // Configura os eventos de clique para todos os ícones de olho
    document.querySelectorAll('.eyes-slashnfill i').forEach(icon => {
        icon.addEventListener('click', function() {
            togglePasswordVisibility(this);
        });
    });
});