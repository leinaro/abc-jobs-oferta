from flask import request
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from flask_restful import Resource
import hashlib
from datetime import datetime
from sqlalchemy.orm import joinedload
import random

from modelos import (
    db,
    Proyecto,
    ProyectoSchema,
)

proyecto_schema = ProyectoSchema()

class VistaProyecto(Resource):
    def post(self):
        nuevo_proyecto = Proyecto(
            nombre=request.json["nombre"],
        )
        db.session.add(nuevo_proyecto)
        db.session.commit()
        return { 
            "mensaje": "proyecto creado exitosamente", 
            "proyecto":  proyecto_schema.dump(nuevo_proyecto)
            }

        
