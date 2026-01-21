import os
from jogoteca import app
from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField, SubmitField, PasswordField


def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa_jogo{id}' in nome_arquivo:
            return nome_arquivo
    return 'capa_padrao.jpg'

def deleta_imagem(id):
    imagem = recupera_imagem(id)
    if imagem != 'capa_padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'],  imagem))

class FormularioJogo(FlaskForm):
    nome = StringField(
        'Nome do Jogo',
        [validators.DataRequired(), validators.Length(min=1, max=50)]
    )
    categoria = StringField(
        'Categoria',
        [validators.DataRequired(), validators.Length(min=1, max=40)]
    )
    console = StringField(
        'Console',
        [validators.DataRequired(), validators.Length(min=1, max=20)]
    )
    ano_lancamento = IntegerField(
        'Ano de Lançamento',
        [validators.DataRequired(), validators.NumberRange(min=1950, max=2026)]
    )
    salvar = SubmitField('Salvar')

class FormularioUsuario(FlaskForm):
    nickname = StringField(
        'Nickname',
        [validators.DataRequired(), validators.Length(min=1, max=8)]
    )
    senha = PasswordField(
        'Senha',
        [validators.DataRequired(), validators.Length(min=1, max=100)]
    )
    login = SubmitField('Login')
