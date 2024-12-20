# application/blueprints/webui/__init__.py
from flask import Blueprint

webui_bp = Blueprint(
    'webui', 
    __name__, 
    template_folder='templates',
    )

# Importação das rotas
from .viewer import index, login, register, logout, vendas, caixas, estatistica, estoques, home, produtos, usuarios, pdv

# Registro das rotas
webui_bp.add_url_rule("/", view_func=index)
webui_bp.add_url_rule("/login", view_func=login)
webui_bp.add_url_rule("/register", view_func=register)
webui_bp.add_url_rule("/logout", view_func=logout)
webui_bp.add_url_rule("/vendas", view_func=vendas)
webui_bp.add_url_rule("/caixas", view_func=caixas)
webui_bp.add_url_rule("/estatistica", view_func=estatistica)
webui_bp.add_url_rule("/estoques", view_func=estoques)
webui_bp.add_url_rule("/home", view_func=home)
webui_bp.add_url_rule("/produtos", view_func=produtos)
webui_bp.add_url_rule("/usuarios", view_func=usuarios)
webui_bp.add_url_rule("/pdv", view_func=pdv)