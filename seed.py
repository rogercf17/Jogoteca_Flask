from jogoteca import app, db, bcrypt
from models import Usuarios

with app.app_context():
    usuarios = [
        Usuarios(nome='Roger Cardoso', nickname='rogercf',
                 senha=bcrypt.generate_password_hash('alohomora').decode('utf-8')),
        Usuarios(nome='Belisa Barbosa', nickname='besantos',
                 senha=bcrypt.generate_password_hash('coelhinha').decode('utf-8')),
    ]

    db.session.add_all(usuarios)
    db.session.commit()

    print('Usuários seed inseridos com sucesso!')
