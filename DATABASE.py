import sqlite3
import os

# Caminho do banco
DB_DIR = r"C:\Users\998096\Documents\python\PROJETO_TURMA_RH_SENAC\DATA"
DB_PATH = os.path.join(DB_DIR, 'REGISTER_POINTS.db')

# Criação da pasta, se não existir
if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR)


def criar_banco_e_tabelas():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 🏛️ Criação da tabela de colaboradores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Colaborador (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT NOT NULL,
            Codigo TEXT NOT NULL UNIQUE,
            Idade TEXT,
            DataNascimento TEXT,
            CPF TEXT,
            RG TEXT,
            Cargo TEXT,
            SalarioFixo TEXT,
            SalarioHora TEXT,
            DataAdmissao TEXT,
            DataDemissao TEXT
        )
    ''')

    # 🕒 Criação da tabela de registros de ponto
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS RegistroPonto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ColaboradorID INTEGER,
            Data TEXT,
            Hora TEXT,
            Tipo TEXT,
            FOREIGN KEY (ColaboradorID) REFERENCES Colaborador(id)
        )
    ''')

    conn.commit()
    conn.close()
    print('Banco e tabelas verificados/criados com sucesso!')


# ⚙️ Executa sempre ao abrir o sistema
criar_banco_e_tabelas()
