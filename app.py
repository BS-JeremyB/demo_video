from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager



#Initialisation de l'application 
app = Flask(__name__)
app.config.from_object(Config)


#Initialisation de la DB
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#Configuration de flask-login
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

#Charger l'utilisateur depuis la base de données
from models.user_model import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#Importation des blueprints
from routes.movie_routes import movie_bp
from routes.director_routes import director_bp
from routes.auth_routes import auth_bp
from routes.main_routes import main_bp

#Enregistrement des blueprints
app.register_blueprint(movie_bp)
app.register_blueprint(director_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)


if __name__ == '__main__':
    app.run(debug=True)

