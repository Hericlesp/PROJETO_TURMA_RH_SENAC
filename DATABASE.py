import sqlite3
import os

# Caminho do banco
DB_DIR = r"C:\Users\998096\Documents\python\PROJETO_TURMA_RH_SENAC\DATA"
DB_PATH = os.path.join(DB_DIR, 'database.db')

# Criação da pasta, se não existir
if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR)


def criar_banco_e_tabelas():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 🏛️ Tabela de cadastro dos funcionários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cadastros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            matricula INTEGER UNIQUE NOT NULL,
            contato INTEGER,
            idade INTEGER,
            data_nascimento TEXT,
            cpf INTEGER,
            rg INTEGER,
            tipo_contratacao TEXT CHECK (tipo_contratacao IN ('Fixa', 'Horista')),
            cargo TEXT,
            salario REAL,
            data_admissao TEXT,
            ativo TEXT CHECK (ativo IN ('Sim', 'Não')) DEFAULT 'Sim'
        )
    ''')

    # 🕒 Tabela de registro de ponto
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registro_ponto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            colaborador_id INTEGER,
            data TEXT,
            hora TEXT,
            tipo TEXT CHECK (tipo IN ('Entrada', 'Saída')),
            FOREIGN KEY (colaborador_id) REFERENCES cadastros(id)
        )
    ''')

    # 🗂️ Tabela de códigos gerados (HISTÓRICO COMPLETO DOS CÓDIGOS)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registros_codigos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            colaborador_id INTEGER,
            data TEXT,
            hora TEXT,
            codigo TEXT,
            tipo TEXT CHECK (tipo IN ('Entrada', 'Almoço', 'Retorno', 'Saída')),
            status TEXT CHECK (status IN ('Ativo', 'Expirado')) DEFAULT 'Ativo',
            FOREIGN KEY (colaborador_id) REFERENCES cadastros(id)
        )
    ''')

    # 👤 Tabela de usuários (login de acesso ao sistema)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            matricula INTEGER UNIQUE NOT NULL,
            senha TEXT NOT NULL,
            cargo TEXT CHECK (cargo IN ('ADM', 'USER', 'ROOT')) NOT NULL
        )
    ''')

    # 🔧 Inserir usuário administrador padrão, se não existir
    cursor.execute('SELECT * FROM usuarios WHERE matricula = ?', (998096,))
    if not cursor.fetchone():
        cursor.execute('''
            INSERT INTO usuarios (matricula, senha, cargo)
            VALUES (?, ?, ?)
        ''', (998096, '998096', 'ROOT'))

    conn.commit()
    conn.close()
    print('Banco de dados e tabelas criadas/verificadas com sucesso!')


# Executa a criação do banco sempre que roda
criar_banco_e_tabelas()
