let visor = document.getElementById('visor');
let expressao = "";
let memoria_n1 = null; 
let operacaoPendente = "";
let resultadoExibido = false;

async function apertarBotao(botao) {
    // .trim() remove espaços invisíveis antes ou depois do texto do botão!
    let valor = botao.innerText.trim(); 

    botao.classList.add('ativo');
    setTimeout(() => botao.classList.remove('ativo'), 200);

    if (valor === 'C') {
        expressao = "";
        memoria_n1 = null;
        operacaoPendente = "";
        resultadoExibido = false;
        visor.innerText = "0";
    } 
    else if (valor === '=') {
        if (operacaoPendente === 'hyp') {
            enviarParaPython('hyp', memoria_n1, visor.innerText.trim());
            operacaoPendente = "";
        } else if (expressao !== "") {
            enviarParaPython('basica', expressao);
        }
    } 
    else if (botao.classList.contains('btn-cientifico')) {
        if (valor === 'hyp') {
            memoria_n1 = visor.innerText.trim();
            operacaoPendente = 'hyp';
            expressao = "";
            visor.innerText = "Próximo nº...";
        } else {
            let tipo = traduzirTipo(valor);
            enviarParaPython(tipo, visor.innerText.trim());
        }
    }
    else {
        if (visor.innerText === "Próximo nº..." || resultadoExibido) {
            visor.innerText = "";
            expressao = "";
            resultadoExibido = false;
        }
        
        if (valor === '×') valor = '*';
        if (valor === '÷') valor = '/';

        expressao += valor;
        visor.innerText = expressao;
    }
}

function traduzirTipo(v) {
    if (v === '√') return 'raiz';
    if (v === 'x!') return 'fat';
    if (v === 'sin') return 'sin';
    if (v === 'cos') return 'cos';
    if (v === 'tan') return 'tan';
    return ''; // Se retornar vazio, é porque o texto não bateu
}

async function enviarParaPython(tipo, v1, v2 = "0") {
    try {
        let url = `http://127.0.0.1:5000/api/calcular?tipo=${tipo}`;
        
        if (tipo === 'basica') {
            url += `&expressao=${encodeURIComponent(v1)}`;
        } else if (tipo === 'hyp') {
            url += `&n1=${encodeURIComponent(v1)}&n2=${encodeURIComponent(v2)}`;
        } else {
            url += `&n1=${encodeURIComponent(v1)}`;
        }
        
        const resposta = await fetch(url);
        const dados = await resposta.json();
        
        visor.innerText = dados.resultado;
        expressao = dados.resultado.toString();
        resultadoExibido = true;
    } catch (e) {
        visor.innerText = "Erro";
        console.error("Erro no Fetch:", e);
    }
}