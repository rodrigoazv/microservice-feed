from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db

class Teste(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name_teste = db.Column('name_teste', db.String(150))
    def __init__(self, name_teste):
        self.name_teste