from flask import render_template, redirect, url_for
from . import webui_bp

@webui_bp.route('/')
def index():
    return render_template('index.html')

@webui_bp.route('/login')
def login():
    return render_template('login.html')