from flask_marshmallow import Marshmallow
from .model import Teste

ma = Marshmallow()

def configure(app):
    ma.init_app(app)

class TesteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Teste
        load_instance = True