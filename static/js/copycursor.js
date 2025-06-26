document.addEventListener('DOMContentLoaded', function () {
    const links = document.querySelectorAll('a.link-copy');

    links.forEach(link => {
        link.addEventListener('click', function (event) {
            event.preventDefault();

            // Copiar o texto, excluindo possíveis ícones
            const tempNode = this.cloneNode(true);
            const iconInClone = tempNode.querySelector('i');
            if (iconInClone) iconInClone.remove();
            const textToCopy = tempNode.textContent.trim();

            navigator.clipboard.writeText(textToCopy)
                .then(() => {
                    mostrarIcone(this, 'bi-check-lg', 'text-success');
                })
                .catch(() => {
                    mostrarIcone(this, 'bi-x-circle', 'text-danger');
                });
        });
    });

    function mostrarIcone(link, iconeClasse, corClasse) {
        // Remove qualquer ícone anterior
        let icon = link.querySelector('i');
        if (!icon) {
            icon = document.createElement('i');
            icon.style.marginLeft = '8px'; // espaço entre texto e ícone
            link.appendChild(icon);
        }
        icon.className = `bi ${iconeClasse} ${corClasse}`;

        // Remove o ícone após 1,5 segundo
        setTimeout(() => {
            if (icon) icon.remove();
        }, 1500);
    }
});