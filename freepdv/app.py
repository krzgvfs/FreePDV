from flask import Flask
from flask_session import Session

from freepdv.extensions import config, auth 
from freepdv.extensions.database import db

from freepdv.blueprints.webui import webui_bp

def create_app():

    # Definição global do path para static
    app = Flask(__name__, static_folder=r'C:\\Users\\krzgv\\OneDrive\\Área de Trabalho\\Projects\\Projeto Free PDV\\FreePDV\\freepdv\\static')

    app.secret_key = 'admin'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Boa prática para evitar avisos

    # Distribuição da instancia do app principal
    config.init_app(app)
    db.init_app(app)
    auth.init_app(app)

    # Configuração do tipo de sessão
    app.config["SESSION_TYPE"] = "filesystem"

    # Configura a sessão com Flask-Session
    Session(app)
    
    with app.app_context(): 
        db.create_all()

    # Registra o blueprint
    app.register_blueprint(webui_bp)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
