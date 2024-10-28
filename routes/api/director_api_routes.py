from flask import Blueprint
from app import db
from controllers.director_controller import DirectorController

#Blueprint pour API

director_api_bp = Blueprint('directors_api', __name__)

director_api_bp.route('/directors', methods=['GET'])(DirectorController.list_directors)
director_api_bp.route('/directors', methods=['POST'])(DirectorController.add_director)