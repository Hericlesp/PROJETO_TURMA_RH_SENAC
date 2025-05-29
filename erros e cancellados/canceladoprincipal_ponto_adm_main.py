import tkinter as tk
from tkinter import *
from tkinter import ttk
import datetime as dt
import sqlite3
import ponto_user_main as pu
#import python.PROJETO_TURMA_RH_SENAC.errocenter_register as errocenter_register

# caixa de dialogo Hp
from tkinter import messagebox
import os

#CAMINHO PARA O BANCO DE DADOS
DB_DIR = r"C:\Users\998096\Documents\python\PROJETO_TURMA_RH_SENAC\DATA"
#DB_DIR = r"C:\Users\Justino\Documents\Hexa\git&github\PROJETO_TURMA_RH_SENAC\DATA"
DB_PATH = os.path.join(DB_DIR, 'REGISTER_POINTS.db')



    

class SistemaPonto:
    
    #CRIAR BANCO DE DADOS

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
        self.root.geometry("450x450")
        self.root.minsize(450, 450)
        self.root.resizable(True, True)
        self.root.configure(bg="green")
        #self.root.iconbitmap(r'C:\Users\998096\Documents\python\PROJETO_TURMA_RH_SENAC\ponto_main.py')
        #self.root.iconbitmap(r'C:\Users\Justino\Documents\Hexa\git&github\PROJETO_TURMA_RH_SENAC\pin.png')

        self.criar_widgets()

    def criar_widgets(self):
        # Barra superior
        self.top_frame = tk.Frame(self.root, bg="green", width=900)
        self.top_frame.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)

        self.title_lbl = tk.Label(self.top_frame, text="HexAluv", font=("Arial", 20,"bold"), bg="green", fg="white")
        self.title_lbl.grid(row=0, column=3, padx=10, pady=10)

        # Frame lateral (Menu)
        self.menu_frame = tk.Frame(self.root, bg="#d9d9d9", width=150)
        self.menu_frame.grid(row=1, column=0, sticky="ns", padx=0, pady=15)

        # Botões do menu
        btn_home = tk.Button(self.menu_frame, text="Home", bg="#f0f0f0", width=15)
        btn_home.grid(pady=10)

        btn_cadastro = tk.Button(self.menu_frame, text="Cadastro", bg="#f0f0f0", width=15,)
        btn_cadastro.grid(pady=10)

        btn_registrar = tk.Button(self.menu_frame, text="Registrar \n Ponto", bg="#f0f0f0", width=15,)
        btn_registrar.grid(pady=10)

        btn_sair = tk.Button(self.menu_frame, text="Sair", bg="#f0f0f0", width=15, command=self.root.quit)
        btn_sair.grid(pady=10)


        # Frame do centro
        self.center_frame = tk.Frame(self.root, bg="white")
        self.center_frame.grid()



    def opcoes(self):
        bl_frame = tk.Frame(self.root, bg= "blue", fg= "black", width= 100 )
        bl_frame.grid( fill="y", side="right")
        
        
        txt_lbl = tk.Label(bl_frame, text="hello", fg="black").pack()

    def run(self):
        self.root.mainloop()

# Programa principal
if __name__ == "__main__":
    root = tk.Tk()
    point = SistemaPonto(root)
    point.run()
