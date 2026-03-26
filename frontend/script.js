const BASE_URL = 'http://127.0.0.1:8000/api/';

function mostrarSecao(idSecao) {
    document.querySelectorAll('main section').forEach(section => {
        section.style.display = 'none';
    });

    const secaoAtiva = document.getElementById(idSecao);
    if (secaoAtiva) {
        secaoAtiva.style.display = 'block';
    }
}

async function carregarDados(endpoint, tabelaId, formatarLinha) {
    const corpoTabela = document.getElementById(tabelaId);
    try {
        const resposta = await fetch(`${BASE_URL}${endpoint}/`);
        if (!resposta.ok) throw new Error(`Erro ao aceder a ${endpoint}`);

        const dados = await resposta.json();

        const lista = dados.results ? dados.results : dados;

        corpoTabela.innerHTML = '';
        lista.forEach(item => {
            const linha = document.createElement('tr');
            linha.innerHTML = formatarLinha(item);
            corpoTabela.appendChild(linha);
        });
    } catch (erro) {
        console.error(erro);
    }
}

document.querySelectorAll('nav a').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();

        const secaoAlvo = link.getAttribute('href').substring(1);
        
        mostrarSecao(secaoAlvo);

        if (secaoAlvo === 'estudantes') {
            carregarDados('estudantes', 'tabela-estudantes-corpo', (est) => `
                <td>${est.id}</td>
                <td>${est.nome}</td>
                <td>${est.email}</td>
            `);
        } 
        else if (secaoAlvo === 'cursos') {
            carregarDados('cursos', 'tabela-cursos-corpo', (cur) => `
                <td>${cur.id}</td>
                <td>${cur.nome}</td>
                <td>${cur.vagas}</td>
            `);
        } 
        else if (secaoAlvo === 'matriculas') {
            // AJUSTE AQUI: Use os nomes dos campos do seu Model de Matrícula
            carregarDados('matriculas', 'tabela-matriculas-corpo', (mat) => `
                <td>${mat.id}</td>
                <td>${mat.estudante}</td>
                <td>${mat.curso}</td>
            `);
        }
    });
});

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('main section').forEach(s => s.style.display = 'none');
});