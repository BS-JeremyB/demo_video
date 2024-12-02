from flask import request, jsonify
from models.user_model import User
from schemas.user_schema import user_schema
from services.session_scope import session_scope
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from datetime import timedelta

class UserController:

    @staticmethod
    def register():
        data = request.get_json()
        validated_data = user_schema.load(data)
        password_hashed = generate_password_hash(validated_data['password_hash'])
        validated_data['password_hash'] = password_hashed
        user = User(**validated_data)

        with session_scope() as session:
            session.add(user)
            session.flush()
            return jsonify(user_schema.dump(user)), 201
        

    @staticmethod
    def login_user():
        data = request.get_json()
        with session_scope() as session:
            user = session.query(User).filter_by(email=data['email']).first()
            if user and check_password_hash(user.password_hash, data['password_hash']):

                claims = {
                    'username': user.username
                }

                access_token = create_access_token(identity=user.id, additional_claims=claims, expires_delta=timedelta(hours=2))
                return jsonify(access_token=access_token),200
            return jsonify(message='invialid credentials'),401

                
