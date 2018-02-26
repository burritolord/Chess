from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from src.config import Config
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
Session(app)
socketio = SocketIO(app, manage_session=False)

db.init_app(app)
socketio.init_app(app)
# socketio.run(app)

from src import routes
from src.models import *
