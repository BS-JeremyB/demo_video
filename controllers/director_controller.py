from flask import request, jsonify
from models.director_model import Director
from services.session_scope import session_scope
from schemas.director_schema import director_schema, directors_schema


class DirectorController:
    @staticmethod
    def list_directors():
        with session_scope() as session:
            directors = session.query(Director).all()
            return directors_schema.dump(directors), 200



    @staticmethod
    def add_director():
        data = request.get_json()
        validated_data = director_schema.load(data)
        director = Director(**validated_data)

        with session_scope() as session:
            session.add(director)
            session.flush()
            return director_schema.dump(director), 201