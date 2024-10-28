from flask import Blueprint
from controllers.movie_controller import MovieController

movie_api_bp = Blueprint('movies_api', __name__)

movie_api_bp.route('/movies', methods=['GET'])(MovieController.list_movies)