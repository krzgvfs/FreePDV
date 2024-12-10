from flask import render_template, redirect, url_for
from . import webui_bp

@webui_bp.route('/')
def index():
    #if not auth_manager.get_user():
    #    return redirect(url_for('auth.login'))
    return render_template('index.html')