import tkinter as tk
from tkinter import *
import sqlite3
import datetime as dt
import os

#documentos internos
import registro_funcionario
import help
import POINT_registrar as point


# Caminho para o banco de dados
DB_DIR = r"C:\Users\998096\Documents\python\PROJETO_TURMA_RH_SENAC\DATA"
DB_PATH = os.path.join(DB_DIR, 'REGISTER_POINTS.db')


class SistemaPonto:

    def criar_banco():
        if not os.path.exists(DB_DIR):
            os.makedirs(DB_DIR)

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS Colaborador (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            RA INT UNIQUE,
            Nome TEXT,
            Setor TEXT,
            Email TEXT,
            Celular INT
        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS Entrada (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            HORA_ENT TEXT,
            STATUS TEXT DEFAULT 'WORKING'
        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS Saida (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            HORA_SAI TEXT,
            STATUS TEXT DEFAULT 'EXIT'
        )''')

        conn.commit()
        conn.close()

    def __init__(self, root):
        self.root = root
        self.root.title("Registro de ponto")
        self.root.geometry("700x500")
        self.root.minsize(700, 500)
        self.root.resizable(True, True)
        self.root.configure(bg="white")

        self.criar_widgets()

    def criar_widgets(self):
        # Barra superior
        self.top_frame = tk.Frame(self.root, bg="green", height=70)
        self.top_frame.pack(fill="x", side="top")

        self.title_lbl = tk.Label(self.top_frame, text="HEXALUV", font=("Arial", 20, "bold"), bg="green", fg="white")
        self.title_lbl.pack(padx=10, pady=15)

        # Frame lateral (Menu)
        self.menu_frame = tk.Frame(self.root, bg="#d9d9d9", width=150)
        self.menu_frame.pack(fill="y", side="left")

        # Botões do menu lateral
        btn_cadastro = tk.Button(self.menu_frame, text="✏️ | Cadastro", bg="#f0f0f0", width=15, command=registro_funcionario.RegistroFuncionario)
        btn_cadastro.pack(pady=10)

        btn_registrar = tk.Button(self.menu_frame, text="⚪ | Registrar \n Ponto", bg="#f0f0f0", width=15, command=point.Point)
        btn_registrar.pack(pady=10)
        
        btn_home = tk.Button(self.menu_frame, text="🛟 | Help", bg="#f0f0f0", width=15, command=help.help.infohelp)
        btn_home.pack(pady=10)
            
        btn_sair = tk.Button(self.menu_frame, text="🚪 | Sair", bg="#f0f0f0", width=15, command=self.root.quit)
        btn_sair.pack(pady=10)

        # Frame do centro
        self.center_frame = tk.Frame(self.root, bg="white")
        self.center_frame.pack(fill="both", side="left", expand=True, padx=0, pady=15)
        
    

        # self.nome_lbl = tk.Label(self.center_frame, text="José Araudo Dos Santos", font=("Arial", 20), bg="white", fg="black")
        # self.nome_lbl.pack(padx=10)

        # self.Matricula_lbl = tk.Label(self.center_frame, text="MATRICULA: 85b690", font=("Arial", 10), bg="white", fg="black")
        # self.Matricula_lbl.pack(padx=10)

        # self.codigo_lbl = tk.Label(self.center_frame, text="CÓDIGO", font=("Arial", 14, "bold"), bg="white", fg="black")
        # self.codigo_lbl.pack(padx=10, pady=10)

        # self.codigo_ety = tk.Entry(self.center_frame, font=("Arial", 20, "bold"), bg="#f0f0f0", fg="black", width=15, justify="center")
        # self.codigo_ety.pack(pady=20)

        # # Footer frame
        # self.footer_frame = tk.Frame(self.root, bg="white")
        # self.footer_frame.pack(fill="both", padx=0, pady=10)

        # self.Regis_Entrada_btn = tk.Button(self.center_frame, text="Registrar \nEntrada", font=("Arial", 14), bg="#0300A7", fg="white", width=20, height=2)
        # self.Regis_Entrada_btn.pack(pady=10)

    def run(self):
        self.root.mainloop()


# Programa principal
if __name__ == "__main__":
    root = tk.Tk()
    point = SistemaPonto(root)
    point.run()
