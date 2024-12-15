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

@webui_bp.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'GET':
        return render_template('registrar.html')
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
