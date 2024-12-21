from flask import Flask, request ,render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from . import webui_bp

from freepdv.extensions.database import db
from freepdv.extensions import auth 
from freepdv.models import User

@webui_bp.route('/')
@login_required
def index():
    return render_template('index.html')

@webui_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        nome = request.form['nomeForm']
        senha = request.form['senhaForm']

        novo_usuario = User(nome=nome, senha=auth.hash(senha))
        db.session.add(novo_usuario)
        db.session.commit()

        login_user(novo_usuario)

    return redirect(url_for('webui.index'))

@webui_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        nome = request.form['nomeForm']
        senha = request.form['senhaForm']
    
        user = db.session.query(User).filter_by(nome=nome, senha=auth.hash(senha)).first()

        if not user:
            return 'Nome ou senha incorreto'

        login_user(user)

        return redirect(url_for('webui.index'))

@webui_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('webui.login'))


@webui_bp.route('/vendas')
@login_required
def vendas():
    return render_template('vendas.html')

@webui_bp.route('/home')
@login_required
def home():
    return render_template('home.html')

@webui_bp.route('/caixas')
@login_required
def caixas():
    return render_template('caixas.html')

@webui_bp.route('/estatistica')
@login_required
def estatistica():
    return render_template('estatistica.html')

@webui_bp.route('/estoques')
@login_required
def estoques():
    return render_template('estoques.html')

@webui_bp.route('/produtos')
@login_required
def produtos():
    return render_template('produtos.html')

@webui_bp.route('/usuarios')
@login_required
def usuarios():
    return render_template('usuarios.html')

@webui_bp.route('/pdv')
@login_required
def pdv():
    return render_template('pdv.html')

@webui_bp.route('/combo')
@login_required
def combo():
    return render_template('combo.html')