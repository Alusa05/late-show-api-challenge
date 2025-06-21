import os

SQLALCHEMY_DATABASE_URI = "postgresql://alusa:051598@localhost:5432/late_show_db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'super-secret')