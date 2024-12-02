from flask import Blueprint
from controllers.user_controller import UserController

auth_api_bp = Blueprint("auth_api", __name__)

auth_api_bp.route('/auth/register', methods=['POST'])(UserController.register)
auth_api_bp.route('/auth/login', methods=['POST'])(UserController.login_user)
