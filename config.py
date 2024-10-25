import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/flaskdemo_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True