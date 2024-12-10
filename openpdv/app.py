from flask import Flask
from flask_session import Session

from openpdv.extensions import config
from openpdv.blueprints.webui import webui_bp

def create_app():

    # Definição global do path para static
    app = Flask(__name__, static_folder=r'openpdv\\static')

    # Distribuição da instancia do app principal
    config.init_app(app)

    # Configuração do tipo de sessão
    app.config["SESSION_TYPE"] = "filesystem"

    # Configura a sessão com Flask-Session
    Session(app)
    
    # Registra o blueprint
    app.register_blueprint(webui_bp)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
