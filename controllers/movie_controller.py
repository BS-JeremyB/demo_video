from flask import request, jsonify
from models.movie_model import Movie
from schemas.movie_schema import movie_schema, movies_schema
from services.session_scope import session_scope

class MovieController:

    @staticmethod
    def list_movies():
        with session_scope() as session:
            movies = session.query(Movie).all()
            return movies_schema.dump(movies), 200