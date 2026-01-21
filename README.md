# 🎮 Jogoteca Flask

Projeto web desenvolvido em **Flask** para gerenciamento de jogos, com autenticação de usuários, cadastro, listagem e persistência em banco de dados.

A aplicação foi criada com foco educacional e prática de conceitos de **Flask**, **SQLAlchemy**, **deploy em produção** e **boas práticas de configuração com variáveis de ambiente**.

---

## 🚀 Funcionalidades

- Cadastro e listagem de jogos
- Sistema de login e autenticação de usuários
- Proteção contra CSRF
- Criptografia de senhas com Bcrypt
- Upload de imagens
- Persistência em banco de dados relacional
- Deploy em produção usando Render

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.12+**
- **Flask**
- **Flask-SQLAlchemy**
- **Flask-WTF**
- **Flask-Bcrypt**
- **PostgreSQL** (produção)
- **Gunicorn**
- **python-dotenv**
- **HTML + Jinja2**

---

## 📁 Estrutura do Projeto

```
jogoteca/
│── jogoteca.py
│── config.py
│── models.py
│── views_game.py
│── views_user.py
│── templates/
│── static/
│── uploads/
│── requirements.txt
│── Procfile
│── .env (não versionado)
```

---

## ⚙️ Configuração do Ambiente

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/jogoteca-flask.git
cd jogoteca-flask
```

### 2️⃣ Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 🔐 Variáveis de Ambiente (.env)

Crie um arquivo `.env` na raiz do projeto:

```env
SECRET_KEY=sua_chave_secreta
DATABASE_URL=postgresql://usuario:senha@host:porta/database
```

> ⚠️ **Nunca versionar o arquivo `.env`**

---

## ▶️ Executando Localmente

```bash
python jogoteca.py
```

Acesse:
```
http://127.0.0.1:5000
```

---

## ☁️ Deploy em Produção (Render)

### 📄 Procfile

```
web: gunicorn jogoteca:app
```

### 🔧 Configurações no Render

- **Build Command:**
  ```bash
  pip install -r requirements.txt
  ```

- **Start Command:**
  ```bash
  gunicorn jogoteca:app
  ```

- Definir variáveis de ambiente:
  - `SECRET_KEY`
  - `DATABASE_URL`

---

## 🗄️ Banco de Dados

As tabelas são criadas automaticamente com:

```python
with app.app_context():
    db.create_all()
```

---

## 🔒 Segurança

- Senhas criptografadas com **Bcrypt**
- Proteção CSRF ativa
- Credenciais sensíveis protegidas por variáveis de ambiente

---

## 📚 Aprendizados do Projeto

- Deploy real de aplicação Flask
- Configuração correta de banco em produção
- Uso de variáveis de ambiente
- Debug de erros 500 em produção
- Integração Flask + PostgreSQL

---

## 👤 Autor

**Roger Cardoso Ferreira**
* GITHUB - (https://github.com/rogercf17)
* LINKEDIN - (https://www.linkedin.com/in/roger-cardoso-030565212/)

---

## 📜 Licença

Este projeto é de uso livre para estudos e aprendizado.

