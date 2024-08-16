from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aula')
# / é um decorador para definir a rota das nossas páginas.
@app.route('/aula/<nome>')
@app.route('/aula/<nome>/<curso>')
@app.route('/aula/<nome>/<curso>/<int:ano>')
def aula(nome = 'Maria', curso = 'Info', ano =1):
    dados = {'nome': nome, 'curso': curso, 'ano': ano}
    return render_template('aula.html', dados_html = dados)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/dados', methods=["POST"])
def dados():
    dados = request.form
    idade = int(request.form["idade"])
    # request serve para carregar os dados de um formulário enviado. Utilizado para passar seus dados à uma outra página. 
    return render_template('dados.html', dados = dados, idade = idade)


if __name__ == '__main__':
    app.run()

