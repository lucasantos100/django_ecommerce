// darkmode.js
document.addEventListener('DOMContentLoaded', function () {
    // Verifica se o modo escuro está ativado no localStorage
    const modoEscuro = localStorage.getItem('modoEscuro') === 'true';

    // Se estiver no modo escuro, aplica a classe dark-mode
    if (modoEscuro) {
        document.body.classList.add('dark-mode');
    }

    // Evento de clique no botão de alternar modo
    const modoClaroBtn = document.getElementById('modo-claro');
    if (modoClaroBtn) {
        modoClaroBtn.addEventListener('click', function () {
            document.body.classList.toggle('dark-mode');
            
            // Armazena a preferência do usuário no localStorage
            const isDarkMode = document.body.classList.contains('dark-mode');
            localStorage.setItem('modoEscuro', isDarkMode);
        });
    }
});

function toggleSobre() {
    var conteudo = document.querySelector('.sobre-conteudo');
    conteudo.style.display = conteudo.style.display === 'block' ? 'none' : 'block';
}

// Função para verificar se o elemento está visível na tela
function isElementInViewport(el) {
    const rect = el.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

// Função que adiciona a classe "visible" quando o elemento entra na tela
function handleScroll() {
    const elements = document.querySelectorAll('.animate-on-scroll');
    elements.forEach(el => {
        if (isElementInViewport(el)) {
            el.classList.add('visible');
        }
    });
}

// Adiciona o evento de scroll
window.addEventListener('scroll', handleScroll);

// Controla o menu de acessibilidade
function toggleAcessibilidadeMenu() {
    const menu = document.querySelector('.acessibilidade-options');
    menu.classList.toggle('show');
}

// Aumentar fonte
let fontSize = 16; // Tamanho base
function aumentarFonte() {
    fontSize += 2;
    document.body.style.fontSize = `${fontSize}px`;
}

// Diminuir fonte
function diminuirFonte() {
    fontSize = Math.max(12, fontSize - 2); // Limite mínimo de 12px
    document.body.style.fontSize = `${fontSize}px`;
}

// Ativar/desativar alto contraste
function toggleContraste() {
    document.body.classList.toggle('alto-contraste');
}

// Resetar as alterações
function resetarAlteracoes() {
    // Resetar o tamanho da fonte para o valor padrão
    fontSize = 16; // Restabelece o tamanho original
    document.body.style.fontSize = `${fontSize}px`;

    // Remover a classe de alto contraste, caso esteja ativada
    if (document.body.classList.contains('alto-contraste')) {
        document.body.classList.remove('alto-contraste');
    }
}

// Tornar o botão arrastável
const menu = document.getElementById('menu-acessibilidade');
const button = document.getElementById('acessibilidade-btn');

let isDragging = false;
let offsetX = 0;
let offsetY = 0;

button.addEventListener('mousedown', (e) => {
    isDragging = true;
    offsetX = e.clientX - menu.getBoundingClientRect().left;
    offsetY = e.clientY - menu.getBoundingClientRect().top;
    menu.style.cursor = 'grabbing';
});

document.addEventListener('mousemove', (e) => {
    if (isDragging) {
        const x = e.clientX - offsetX;
        const y = e.clientY - offsetY;
        menu.style.left = `${x}px`;
        menu.style.top = `${y}px`;
        menu.style.right = 'auto'; // Remove a fixação no lado direito
        menu.style.bottom = 'auto'; // Garante que só usa top e left
    }
});

document.addEventListener('mouseup', () => {
    isDragging = false;
    menu.style.cursor = 'grab';
});
