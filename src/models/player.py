from src import db, login
from sqlalchemy_utils import PasswordType, EmailType, force_auto_coercion
from flask_login import UserMixin

force_auto_coercion()


class Player(UserMixin, db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    fullname = db.Column(db.String(200), nullable=True)
    email = db.Column(EmailType, unique=True)
    password = db.Column(PasswordType(schemes=['pbkdf2_sha512']), unique=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        """
        Return dictionary version of object
        :return:
        """
        return {
            'id': self.id,
            'username': self.username,
            'fullname': self.fullname,
            'email': self.email,
        }

    def set_password(self, password):
        self.password = password

    def check_password(self, password):
        return self.password == password

    @classmethod
    def load_by_id(cls, player_id):
        return cls.query.get(player_id)

    @classmethod
    def load_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def load_by_email(cls, email):
        return cls.query.filter_by(email=email).first()


@login.user_loader
def load_user(uid):
    return Player.load_by_id(int(uid))
