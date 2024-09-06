#pip install flask
#pip install Flask-SQLAlchemy
#pip install Flask-Migrate
#pip install Flask-Script
#pip install pymysql
#flask db init
#flask db migrate -m "Migração Inicial"
#flask db upgrade

from flask import Flask, render_template, request, flash, redirect
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

@app.route('/usuario/add')
def usuario_add():
    return render_template('usuario_add.html')

@app.route('/usuario/save', methods=['POST'])
def usuario_save():
    nome = request.form.get('nome')
    email = request.form.get('email')
    idade = request.form.get('idade')
    if nome and email and idade:
        usuario = Usuario(nome, email, idade)
        db.session.add(usuario)
        db.session.commit()
        flash('Usuário cadastrado com sucesso!')
        return redirect ("/usuario")
    else:
        flash("Preencha todos os campos!")
        return redirect ("/usuario/add")
    
@app.route('/usuario/remove/<int:id>')
def usuario_remove(id):
    if id > 0:
        usuario = Usuario.query.get(id)
        db.session.delete(usuario)
        db.session.commit()
        flash('Usuário removido com sucesso.')
        return redirect('/usuario')
    else:
        flash('Caminho incorreto, fella!')
        return redirect('/usuario')


@app.route('/usuario/edita/<int:id>')
def usuario_editar(id):
    usuario = Usuario.query.get(id)
    return render_template('usuario_editar.html', dados = usuario)

@app.route('/usuario/editasave', methods = ['POST'])
def usuario_edita_save():
    id = request.form.get('id')
    nome = request.form.get('nome')
    email = request.form.get('email')
    idade = request.form.get('idade')
    if id and nome and email and idade:
        usuario = Usuario.query.get(id)
        usuario.nome = nome
        usuario.email = email
        usuario.idade = idade
        db.session.commit()
        flash('Dados 100 por cento atualizados, é ruim de aturar')
        return redirect('/usuario')
    else:
        flash('Não tem dado na tabela')
        return redirect('/usuario')

if __name__ == '__main__':
    app.run()

