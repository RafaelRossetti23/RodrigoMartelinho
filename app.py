import os
from flask import Flask, render_template
from flask_frozen import Freezer  # Adicione isso aqui

app = Flask(__name__)

p_servico_martelo = 'servicos/martelinho-de-ouro-sorocaba.html'
p_servico_pintura = 'servicos/revitalizacao-pintura-automotiva-sorocaba.html'
p_servicos_outros = 'servicos/outros-servicos-rodrigo-martelinho.html'
p_servicos_higienizacao = 'servicos/limpeza-e-higienizacao-de-carros.html'
p_servicos_hidratacao = 'servicos/hidratacao-de-couro-sorocaba.html'
p_sobre_rodrigo_martelinho = 'rodrigo-martelinho-de-ouro.html'
p_nossos_clientes = 'nossos-clientes.html'
p_fale_conosco = 'fale-com-rodrigo-martelinho-de-ouro.html'
p_dicas = "dicas-martelinho-de-ouro.html"
p_antes_depois_martelinho = 'antes-e-depois/martelinho-de-ouro.html'
p_antes_depois_revitalizacao = 'antes-e-depois/revitalizacao-de-carros.html'
p_antes_depois_higienizacao = 'antes-e-depois/higienizacao-de-carros.html'
p_antes_depois_hidratacao = 'antes-e-depois/hidratacao-de-carros.html'

# COMENTE OU REMOVA ESTA ROTA ABAIXO PARA NÃO DAR ERRO NO BUILD:
# @app.route('/<url_client>')
# def error404(url_client):
#     return render_template("errorpage.html")

@app.route('/')
@app.route('/index.html')
def index():
    teste = "active"
    return render_template("index.html", teste=teste)

@app.route('/'+ p_sobre_rodrigo_martelinho)
def empresa():
    return render_template(p_sobre_rodrigo_martelinho)

@app.route('/'+ p_servico_martelo)
def serv_martelo():
    return render_template(p_servico_martelo)

@app.route('/'+ p_servico_pintura)
def serv_pintura():
    return render_template(p_servico_pintura)

@app.route('/' + p_servicos_hidratacao)
def serv_hidratacao():
    return render_template(p_servicos_hidratacao)

@app.route('/'+p_servicos_higienizacao)
def serv_higi():
    return render_template(p_servicos_higienizacao)

@app.route('/'+p_servicos_outros)
def serv_outros():
    return render_template(p_servicos_outros)

@app.route('/'+p_antes_depois_martelinho)
def a_d_martelinho():
    return render_template(p_antes_depois_martelinho)

@app.route('/'+p_antes_depois_higienizacao)
def a_d_higi():
    return render_template(p_antes_depois_higienizacao)

@app.route('/'+p_antes_depois_hidratacao)
def a_d_hidra():
    return render_template(p_antes_depois_hidratacao)

@app.route('/'+p_antes_depois_revitalizacao)
def a_d_revi():
    return render_template(p_antes_depois_revitalizacao)

@app.route('/'+p_fale_conosco)
def fale_conosco():
    return render_template(p_fale_conosco)

@app.route('/'+p_dicas)
def dicas_martelinho():
    return render_template(p_dicas)

@app.route('/'+p_nossos_clientes)
def clientes_martelinho():
    return render_template(p_nossos_clientes)

# ADICIONE ESSE BLOCO NO FINAL DO SEU ARQUIVO:
freezer = Freezer(app)

if __name__ == '__main__':
    # Se você rodar "python app.py freeze", ele gera o site estático.
    # Se rodar só "python app.py", ele abre o servidor local de testes.
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'freeze':
        freezer.freeze()
    else:
        app.run(debug=True, port=5000)

