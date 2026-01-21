import mysql.connector
from mysql.connector import errorcode
import sys
from flask_bcrypt import generate_password_hash

print('Conectando...')

try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='rogercf',
        password='17010531Roger'
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Existe algo errado no nome de usuário ou senha')
    else:
        print(err)
    sys.exit(1)

cursor = conn.cursor()
cursor.execute("DROP DATABASE IF EXISTS `jogoteca`;")
cursor.execute("CREATE DATABASE `jogoteca`;")
cursor.execute("USE `jogoteca`;")

TABLES = {}
TABLES['jogos'] = ('''
    CREATE TABLE `jogos` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,
      `categoria` varchar(40) NOT NULL,
      `console` varchar(20) NOT NULL,
      `ano_lancamento` int(10) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
''')
TABLES['usuarios'] = ('''
    CREATE TABLE `usuarios` (
      `nome` varchar(20) NOT NULL,
      `nickname` varchar(8) NOT NULL,
      `senha` varchar(100) NOT NULL,
      PRIMARY KEY (`nickname`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
''')

for tabela in TABLES:
    tabela_sql = TABLES[tabela]
    try:
        print('Criando tabela {}:'.format(tabela), end=' ')
        cursor.execute(tabela_sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('Já existe')
        else:
            print(err.msg)
    else:
        print('OK!')

usuarios_sql = 'INSERT INTO usuarios (nome, nickname, senha) VALUES (%s, %s, %s)'
usuarios = [
    ('Roger Cardoso', 'rogercf', generate_password_hash('alohomora').decode('utf-8')),
    ('Belisa Barbosa', 'besantos', generate_password_hash('coelhinha').decode('utf-8')),
    ('Heitor Cardoso', 'heitor18', generate_password_hash('neymar').decode('utf-8'))
]
cursor.executemany(usuarios_sql, usuarios)
cursor.execute('SELECT * FROM jogoteca.usuarios')
print(' -------------  Usuários:  -------------')
for usuario in cursor.fetchall():
    print(usuario[1])


jogos_sql = 'INSERT INTO jogos (nome, categoria, console, ano_lancamento) VALUES (%s, %s, %s, %s)'
jogos = [
    ('Tetris', 'Puzzle', 'Atari', 1985),
    ('God of War', 'Hack n Slash', 'PS2', 2005),
    ('Mortal Kombat', 'Luta', 'PS2', 2012)
]
cursor.executemany(jogos_sql, jogos)
cursor.execute('SELECT * FROM jogoteca.jogos')
print(' -------------  Jogos:  -------------')
for jogo in cursor.fetchall():
    print(jogo[1])

conn.commit()
cursor.close()
conn.close()
