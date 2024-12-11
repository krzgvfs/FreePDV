# application/blueprints/webui/__init__.py
from flask import Blueprint

webui_bp = Blueprint(
    'webui', 
    __name__, 
    template_folder='templates',
    )

# Importação das rotas
from .viewer import index, login

# Registro das rotas
webui_bp.add_url_rule("/", view_func=index)
webui_bp.add_url_rule("/login", view_func=login)