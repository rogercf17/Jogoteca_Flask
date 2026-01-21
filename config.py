import os

SECRET_KEY = os.getenv('SECRET_KEY', 'dev')

DATABASE_URL = os.getenv('DATABASE_URL')

if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

SQLALCHEMY_DATABASE_URI = DATABASE_URL

SQLALCHEMY_TRACK_MODIFICATIONS = False

UPLOAD_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'uploads'
)
