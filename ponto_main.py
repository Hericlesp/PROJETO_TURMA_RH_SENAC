import tkinter as tk
from tkinter import *
from tkinter import ttk
import datetime as dt
import sqlite3


# caixa de dialogo Hp
from tkinter import messagebox
import os

#CAMINHO PARA O BANCO DE DADOS
#DB_DIR = r"C:\Users\998096\Documents\python\PROJETO_TURMA_RH_SENAC\DATA"
DB_DIR = r"C:\Users\Justino\Documents\Hexa\git&github\PROJETO_TURMA_RH_SENAC\DATA"
DB_PATH = os.path.join(DB_DIR, 'REGISTER_POINTS.db')


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
    
#modelo projeto 
# import tkinter as tk

# janela = tk.Tk()
# janela.title("Layout com Vários Frames")

# # Frame do topo
# top_frame = tk.Frame(janela, bg="skyblue")
# top_frame.pack(fill="x")

# # Frame lateral (esquerda)
# left_frame = tk.Frame(janela, bg="lightgreen", width=100)
# left_frame.pack(side="left", fill="y")

# # Frame principal
# main_frame = tk.Frame(janela, bg="white")
# main_frame.pack(side="left", expand=True, fill="both")

# # Adicionando widgets
# tk.Label(top_frame, text="Cabeçalho", bg="skyblue").pack(pady=10)
# tk.Label(left_frame, text="Menu", bg="lightgreen").pack(pady=10)
# tk.Label(main_frame, text="Área principal", bg="white").pack(pady=20)

# janela.mainloop()

#notas importantes
# relief	Estilo da borda (flat, raised, sunken, groove, ridge)
# bd	Espessura da borda


root = tk.Tk()
root.title("Registro de ponto")
root.geometry("900x500")
#formata ção da janela
root.minsize(900, 500)
root.resizable(False, True)
root.configure(bg= "lightblue")
root.iconbitmap(r'C:\Users\Justino\Documents\Hexa\git&github\PROJETO_TURMA_RH_SENAC\pin.png')

#barra de menu
top_frame = tk.Frame(root, bg= "#F09001", width= 900, height= 50)
top_frame.pack(side= "top", fill="x")

title_lbl = tk.Label(top_frame, text= "Ponto Eletrônico", font= ("Arial", 20), bg= "#F09001", fg= "black")
title_lbl.pack(pady=10)


root.mainloop()