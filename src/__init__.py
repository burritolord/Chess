from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from src.config import Config
from flask_sessionstore import Session

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
socketio = SocketIO(app, manage_session=False)
# How do i add session model to migrate script?
session = Session(app)
session.app.session_interface.db.create_all()

db.init_app(app)
socketio.init_app(app)
# socketio.run(app)

from src import routes
from src.models import *
