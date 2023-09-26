import enum
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


db = SQLAlchemy()

class Proyecto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128))


class ProyectoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Proyecto
        load_instance = True

    id = fields.String()
    nombre = fields.String()