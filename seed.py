from random import seed

from jogoteca import app, db, bcrypt
from models import Usuarios

def prepara_banco():
    with app.app_context():
        if Usuarios.query.first():
            print('Seed já executada, ignorando')
            return

        usuarios = [
            Usuarios(nome='Roger Cardoso', nickname='rogercf',
                     senha=bcrypt.generate_password_hash('alohomora').decode('utf-8')),
            Usuarios(nome='Belisa Barbosa', nickname='besantos',
                     senha=bcrypt.generate_password_hash('coelhinha').decode('utf-8')),
        ]

        db.session.add_all(usuarios)
        db.session.commit()
        print('Seed de usuários executado com sucesso!')

if __name__ == '__main__':
    prepara_banco()
