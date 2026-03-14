from flask import Flask, request, jsonify
from flask_cors import CORS
# Suas funções matemáticas
from adad import soma, sub, mult, div, raiz_quadrada, hipotenusa, fatorial, seno, cosseno, tangente

app = Flask(__name__)
CORS(app)

@app.route('/api/calcular', methods=['GET'])
def calcular():
    tipo = request.args.get('tipo', '')
    
    if tipo == 'basica':
        exp = request.args.get('expressao', '')
        try:
            return jsonify({'resultado': eval(exp)})
        except Exception as e:
            print(f"Erro na basica: {e}")
            return jsonify({'resultado': 'Erro'})

    try:
        # Pega a string. Se vier vazia (''), transforma em '0' antes do float
        n1_str = request.args.get('n1', '0')
        n2_str = request.args.get('n2', '0')
        if n1_str == '': n1_str = '0'
        if n2_str == '': n2_str = '0'
        
        n1 = float(n1_str)
        n2 = float(n2_str)
        
        if tipo == 'raiz': res = raiz_quadrada(n1)
        elif tipo == 'fat': res = fatorial(int(n1))
        elif tipo == 'sin': res = seno(n1)
        elif tipo == 'cos': res = cosseno(n1)
        elif tipo == 'tan': res = tangente(n1)
        elif tipo == 'hyp': res = hipotenusa(n1, n2)
        else: return jsonify({'resultado': 'Erro'})

        return jsonify({'resultado': res})
        
    except Exception as e:
        print(f"Erro cientifico: {e}")
        return jsonify({'resultado': 'Erro'})

if __name__ == '__main__':
    app.run(debug=True)