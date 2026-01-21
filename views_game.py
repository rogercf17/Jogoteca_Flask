from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from jogoteca import app, db
from models import Jogos
from helpers import FormularioJogo, recupera_imagem, deleta_imagem
import time

@app.context_processor
def utility_processor():
    return dict(recupera_imagem=recupera_imagem)

@app.route('/')
def index():
    lista = Jogos.query.order_by(Jogos.id)

    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/cadastro')
def cadastro():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('cadastro')))

    form = FormularioJogo()

    return render_template('cadastro-jogo.html', titulo='Novo Jogo', form=form)

@app.route('/criar', methods=['POST',])
def criar():
    form = FormularioJogo(request.form)

    if not form.validate_on_submit():
        return redirect(url_for('cadastro'))

    nome = form.nome.data
    categoria = form.categoria.data
    console = form.console.data
    ano_lancamento = form.ano_lancamento.data

    if Jogos.query.filter_by(nome=nome).first():
        flash('Jogo existente')
        return redirect(url_for('index'))

    novo_jogo = Jogos(nome=nome, categoria=categoria, console=console, ano_lancamento=ano_lancamento)
    db.session.add(novo_jogo)
    db.session.commit()

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    arquivo.save(f'{upload_path}/capa_jogo{novo_jogo.id}-{timestamp}.jpg')

    return redirect(url_for('index'))

@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar', id=id)))

    jogo = Jogos.query.filter_by(id=id).first()

    form = FormularioJogo()
    form.nome.data = jogo.nome
    form.categoria.data = jogo.categoria
    form.console.data = jogo.console
    form.ano_lancamento.data = jogo.ano_lancamento

    capa_jogo = recupera_imagem(id)

    return render_template('editar-jogo.html', titulo='Editar Jogo', id=id, capa_jogo=capa_jogo, form=form)

@app.route('/atualizar', methods=['POST',])
def atualizar():
    form = FormularioJogo(request.form)

    if form.validate_on_submit():
        jogo = Jogos.query.filter_by(id=request.form['id']).first()
        jogo.nome = form.nome.data
        jogo.categoria = form.categoria.data
        jogo.console = form.console.data
        jogo.ano_lancamento = form.ano_lancamento.data
        db.session.add(jogo)
        db.session.commit()

        arquivo = request.files['arquivo']
        upload_path = app.config['UPLOAD_PATH']
        timestamp = time.time()
        deleta_imagem(jogo.id)
        arquivo.save(f'{upload_path}/capa_jogo{jogo.id}-{timestamp}.jpg')

    return redirect(url_for('index'))

@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

    '''jogo = Jogos.query.filter_by(id=id).first()
    db.session.delete(jogo)
    db.session.commit()'''
    Jogos.query.filter_by(id=id).delete()
    db.session.commit()
    flash("Jogo deletado com sucesso!")

    return redirect(url_for('index'))

@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)
