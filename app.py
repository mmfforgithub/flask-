from flask import Flask, render_template, request
from database import db
from flask_migrate import Migrate
from models import Usuario
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

#drive://usuario:senha@servidor/banco_dados
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/flaskg1"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

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

@app.route('/usuario')
def usuario():
    u = Usuario.query.all()
    return render_template('usuario_lista.html', dados = u)


if __name__ == '__main__':
    app.run()

