from flask import Flask, Blueprint, current_app, jsonify , request
from dataclasses import dataclass
from flask_migrate import Migrate
from flask_json import FlaskJSON, JsonError, json_response, as_json
from .serealizers import configure as config_ma
from flask_sqlalchemy import SQLAlchemy
from .model import configure as config_db
from .model import Teste
from .serealizers import TesteSchemas

teste = Blueprint('teste', __name__)

@teste.route('/')
def hello_world():
    test = current_app.db.session.query(Teste).all()
    return TesteSchemas(many=True).jsonify(test), 200

@teste.route('/post', methods=['POST'])
def add():
    tt = TesteSchemas()
    teste = tt.load(request.json)
    
    current_app.db.session.add(teste)
    current_app.db.session.commit()
    return tt.jsonify(teste), 201