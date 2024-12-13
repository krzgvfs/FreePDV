from flask_login import LoginManager

from freepdv.extensions.database import db
from freepdv.models import User

import hashlib

login_manager = LoginManager()

def init_app(app):
    login_manager.init_app(app)
    login_manager.login_view = 'webui.login'

def hash(txt):
    hash_obj = hashlib.sha256(txt.encode('utf-8'))
    return hash_obj.hexdigest()

@login_manager.user_loader
def user_loader(id):
    usuario = db.session.query(User).filter_by(id=id).first()
    return usuario
