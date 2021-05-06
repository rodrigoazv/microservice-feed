from flask_marshmallow import Marshmallow
from marshmallow import fields
from .model import Teste

ma = Marshmallow()

def configure(app):
    ma.init_app(app)

class TesteSchemas(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Teste
        load_instance = True

    name_teste = fields.Str(required=True)