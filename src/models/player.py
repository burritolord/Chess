from src.db import db
from sqlalchemy_utils import PasswordType, EmailType, force_auto_coercion

force_auto_coercion()


class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    fullname = db.Column(db.String(200), nullable=True)
    email = db.Column(EmailType, unique=True)
    password = db.Column(PasswordType(schemes=['pbkdf2_sha512']), unique=False)
