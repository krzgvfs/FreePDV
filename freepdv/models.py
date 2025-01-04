from flask_login import UserMixin
from freepdv.extensions.database import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), unique=True)
    senha = db.Column(db.String())

class Products(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), unique=True)
    description = db.Column(db.String(100))
    preco = db.Column(db.String(10))
    custo = db.Column(db.String(10))
