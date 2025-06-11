// Pega todos os elementos que podem ser clicados para copiar
const elementosCopiaveis = document.querySelectorAll('.copy-text');

elementosCopiaveis.forEach(elemento => {
    elemento.style.cursor = 'pointer'; // Muda o mouse para parecer clicável

    elemento.addEventListener('click', () => {
        // Copia apenas o texto (sem os ícones)
        const textoParaCopiar = elemento.innerText.trim();

        navigator.clipboard.writeText(textoParaCopiar)
            .then(() => {
                // Aqui você pode exibir um feedback, tipo um alert ou um mini popup
                console.log('Texto copiado: ' + textoParaCopiar);
                // ou: alert('Copiado para a área de transferência!');
            })
            .catch(err => {
                console.error('Erro ao copiar o texto: ', err);
            });
    });
});
