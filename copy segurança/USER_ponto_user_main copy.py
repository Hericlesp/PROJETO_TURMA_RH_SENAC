# import tkinter as tk
# from tkinter import *
# from tkinter import ttk
# import datetime as dt



# class SistemaPonto:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Registro de ponto")
#         self.root.geometry("450x450")
#         self.root.minsize(450, 450)
#         self.root.resizable(False, True)
#         self.root.configure(bg="white")
#         #self.root.iconbitmap(r'C:\Users\998096\Documents\python\PROJETO_TURMA_RH_SENAC\pin.png')
#         #self.root.iconbitmap(r'C:\Users\Justino\Documents\Hexa\git&github\PROJETO_TURMA_RH_SENAC\pin.png')

#         self.criar_widgets()

#     def criar_widgets(self):
#         # Barra superior
#         self.top_frame = tk.Frame(self.root, bg="#F09001", width=900, height=100)
#         self.top_frame.pack(fill="x", side="top", padx=0, pady=0)

#         self.title_lbl = tk.Label(self.top_frame, text="Ponto Eletrônico", font=("Arial", 20,"bold"), bg="#F09001", fg="black")
#         self.title_lbl.pack(padx=10, pady=10)


#         #frame do centro
#         self.center_frame = tk.Frame(self.root, bg="white", width=900, height=300)
#         self.center_frame.pack(fill="both", side="top", padx=0, pady=15)

#         self.nome_lbl = tk.Label(self.center_frame, text="José Araudo Dos Santos", font=("Arial", 28), bg="white", fg="black")
#         self.nome_lbl.pack(padx=10)


#         self.Matricula_lbl = tk.Label(self.center_frame, text=" MATRICULA: 85b690", font=("Arial", 10), bg="white", fg="black")
#         self.Matricula_lbl.pack(padx=10)
        
#         self.codigo_lbl = tk.Label(self.center_frame, text="CÓDIGO", font=("Arial", 14,"bold"), bg="white", fg="black")
#         self.codigo_lbl.pack(padx=10, pady=10)

#         codigo_ety = tk.Entry(self.center_frame, font=("Arial", 20, "bold"), bg="#f0f0f0", fg="black", width=15, justify="center") 
#         codigo_ety.pack(pady=20)



#         #footer frame

#         self.footer_frame = tk.Frame(self.root, bg="white", width=900, height=100)
#         self.footer_frame.pack(fill="both", padx=0, pady=10)

#         Regis_Entrada_btn = tk.Button(self.footer_frame, text="Registrar \n Entrada", font=("Arial", 14), bg="#0300A7", fg="white", width=20, height=2)
#         Regis_Entrada_btn.pack(pady=10)


#     def run(self):
#         self.root.mainloop()

# # Programa principal
# if __name__ == "__main__":
#     root = tk.Tk()
#     point = SistemaPonto(root)
#     point.run()




# ''' PRECISAMOS DE:
# * TABELA COM DADOS INDIVIDUAIS DOS FUNCIONARIOS:
#       HORARIO DE ENTRADA
#       HORARIO DE SAIDA
#       HORARIO DE ALMOÇO
      
# * REGISTRO DE PONTO
# * REGISTRO DE FALTA
# * REGISTRO DE ATESTADO
# * REGISTRO DE FERIADO
# '''


import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import os
from datetime import datetime

# 📂 Caminho do banco
DB_DIR = r"C:\Users\998096\Documents\python\PROJETO_TURMA_RH_SENAC\DATA"
DB_PATH = os.path.join(DB_DIR, 'REGISTER_POINTS.db')


class Point:
    def __init__(self, master):
        self.master = master
        self.master.configure(bg="white")
        self.criar_interface()

    def criar_interface(self):
        # 🔄 Limpa o frame
        for widget in self.master.winfo_children():
            widget.destroy()

        tk.Label(
            self.master, text="REGISTRO DE PONTO",
            font=("Arial", 18, "bold"), bg="white"
        ).grid(row=0, column=0, columnspan=4, pady=10)

        # 📑 Campos
        tk.Label(self.master, text="RA:", bg="white").grid(row=1, column=0, sticky="w")
        self.ra_entry = tk.Entry(self.master, width=20)
        self.ra_entry.grid(row=1, column=1, sticky="w")

        tk.Label(self.master, text="Código:", bg="white").grid(row=2, column=0, sticky="w")
        self.codigo_entry = tk.Entry(self.master, width=20)
        self.codigo_entry.grid(row=2, column=1, sticky="w")

        # 🔘 Botões de ponto
        tipos = ["Entrada", "Saída", "Almoço", "Retorno"]
        col = 0
        for tipo in tipos:
            btn = tk.Button(
                self.master, text=tipo, bg="#007ACC", fg="white", width=15,
                command=lambda t=tipo: self.registrar_ponto(t)
            )
            btn.grid(row=3, column=col, padx=5, pady=10)
            col += 1

        # 🔍 Status do dia
        status_btn = tk.Button(
            self.master, text="🔍 Ver Status do Dia",
            bg="#28a745", fg="white", width=25, command=self.status_do_dia
        )
        status_btn.grid(row=4, column=0, columnspan=4, pady=10)

        # 📊 Tabela de status
        self.tree = ttk.Treeview(
            self.master, columns=("RA", "Nome", "Data", "Hora", "Tipo"),
            show="headings", height=10
        )
        self.tree.grid(row=5, column=0, columnspan=4, pady=10)

        for col in ("RA", "Nome", "Data", "Hora", "Tipo"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor="center")

    def conectar(self):
        return sqlite3.connect(DB_PATH)

    def validar_funcionario(self, ra, codigo):
        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, Nome FROM Colaborador WHERE RA=? AND Codigo=?",
            (ra, codigo)
        )
        resultado = cursor.fetchone()
        conn.close()
        return resultado

    def registrar_ponto(self, tipo):
        ra = self.ra_entry.get().strip()
        codigo = self.codigo_entry.get().strip()

        if not ra or not codigo:
            messagebox.showwarning("Atenção", "Preencha RA e Código.")
            return

        funcionario = self.validar_funcionario(ra, codigo)
        if not funcionario:
            messagebox.showerror("Erro", "RA ou Código inválidos.")
            return

        id_funcionario, nome = funcionario
        data_atual = datetime.now().strftime("%Y-%m-%d")
        hora_atual = datetime.now().strftime("%H:%M:%S")

        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO RegistroPonto (id_funcionario, data, hora, tipo)
            VALUES (?, ?, ?, ?)
        ''', (id_funcionario, data_atual, hora_atual, tipo))
        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Sucesso", f"Ponto '{tipo}' registrado para {nome} às {hora_atual}."
        )
        self.status_do_dia()

    def status_do_dia(self):
        # Limpar tabela
        for item in self.tree.get_children():
            self.tree.delete(item)

        data_atual = datetime.now().strftime("%Y-%m-%d")

        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT c.RA, c.Nome, r.data, r.hora, r.tipo
            FROM RegistroPonto r
            JOIN Colaborador c ON r.id_funcionario = c.id
            WHERE r.data = ?
            ORDER BY r.hora ASC
        ''', (data_atual,))
        registros = cursor.fetchall()
        conn.close()

        for reg in registros:
            self.tree.insert("", "end", values=reg)


if __name__ == "__main__":
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)

    # Criar banco e tabelas se não existirem
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Colaborador (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            RA INTEGER UNIQUE,
            Nome TEXT NOT NULL,
            Setor TEXT,
            Email TEXT,
            Celular TEXT,
            Codigo TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS RegistroPonto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_funcionario INTEGER,
            data TEXT,
            hora TEXT,
            tipo TEXT,
            FOREIGN KEY (id_funcionario) REFERENCES Colaborador(id)
        )
    ''')
    conn.commit()
    conn.close()

    root = tk.Tk()
    app = Point(root)
    root.mainloop()