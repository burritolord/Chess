from src import app
from src import db


@app.before_first_request
def create_db():
    db.create_all()
