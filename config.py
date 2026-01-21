'''import os

SECRET_KEY = 'alura'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'rogercf',
        senha = '17010531Roger',
        servidor = 'localhost',
        database = 'jogoteca'
    )

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'''
import os

SECRET_KEY = os.getenv('SECRET_KEY', 'dev')

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

SQLALCHEMY_TRACK_MODIFICATIONS = False

UPLOAD_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'uploads'
)
