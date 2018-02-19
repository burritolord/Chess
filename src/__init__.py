from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from src.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
socketio = SocketIO(app)

db.init_app(app)
socketio.init_app(app)
# socketio.run(app)

from src import routes
from src.models import *
