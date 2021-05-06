from flask import Flask, current_app, jsonify , request
from dataclasses import dataclass
from flask_migrate import Migrate
from flask_json import FlaskJSON, JsonError, json_response, as_json
from .serealizers import configure as config_ma
from flask_sqlalchemy import SQLAlchemy
from .model import configure as config_db
from .model import Teste

from .teste import teste

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(teste)

FlaskJSON(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

config_ma(app)
config_db(app)

db.create_all()

