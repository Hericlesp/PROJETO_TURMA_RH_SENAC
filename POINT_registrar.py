# # import tkinter as tk


# # class Point(tk.Toplevel):
# #     def __init__(self, master=None):
# #         super().__init__(master)
# #         self.title("Cadastro de Funcionário")
# #         self.geometry("450x450")
# #         self.configure(bg='#FFFFFF')
# #         self.criar_interface()

# #     def criar_interface(self):
# #         center_frame = tk.Frame(self, bg="white")
# #         center_frame.pack(fill="both", side="left", expand=True, padx=0, pady=15)

# #         nome_lbl = tk.Label(center_frame, text="José Araudo Dos Santos", font=("Arial", 20), bg="white", fg="black")
# #         nome_lbl.pack(padx=10)

# #         matricula_lbl = tk.Label(center_frame, text="MATRICULA: 85b690", font=("Arial", 10), bg="white", fg="black")
# #         matricula_lbl.pack(padx=10)

# #         codigo_lbl = tk.Label(center_frame, text="CÓDIGO", font=("Arial", 14, "bold"), bg="white", fg="black")
# #         codigo_lbl.pack(padx=10, pady=10)

# #         codigo_ety = tk.Entry(center_frame, font=("Arial", 20, "bold"), bg="#f0f0f0", fg="black", width=15, justify="center")
# #         codigo_ety.pack(pady=20)

# #         # Footer frame
# #         self.footer_frame = tk.Frame(center_frame, bg="white")
# #         self.footer_frame.pack(fill="both", padx=0, pady=10)

# #         self.Regis_Entrada_btn = tk.Button(center_frame, text="Registrar \nEntrada", font=("Arial", 14), bg="#0300A7", fg="white", width=20, height=2)
# #         self.Regis_Entrada_btn.pack(pady=10)

# # # Programa principal
# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     root.title("Menu Principal")
# #     root.geometry("400x200")

# #     tk.Label(root, text="MENU PRINCIPAL", font=("Arial", 16, "bold")).pack(pady=20)

# #     tk.Button(root, text="Abrir Cadastro de Funcionário", width=30, height=2,
# #               command=lambda: Point(master=root)).pack(pady=10)

# #     tk.Button(root, text="Sair", width=30, height=2, command=root.destroy).pack(pady=10)

# #     root.mainloop()

    
# #     '''
# #     gera banco de dado mas  n conecta aos devidos lugares
# #     '''
# #     # def point():
# #     #     DB_DIR = r"C:\Users\998096\Documents\python\PROJETO_TURMA_RH_SENAC\DATA"
# #     #     DB_PATH = os.path.join(DB_DIR, 'REGISTER_POINTS.db')

# #     #     if not os.path.exists(DB_DIR):
# #     #         os.makedirs(DB_DIR)

# #     #     conn = sqlite3.connect(DB_PATH)
# #     #     cursor = conn.cursor()

# #     #     cursor.execute('''CREATE TABLE IF NOT EXISTS Colaborador (
# #     #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# #     #         RA INT UNIQUE,
# #     #         Nome TEXT,
# #     #         Setor TEXT,
# #     #         Email TEXT,
# #     #         Celular INT
# #     #     )''')

# #     #     cursor.execute('''CREATE TABLE IF NOT EXISTS Entrada (
# #     #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# #     #         HORA_ENT TEXT,
# #     #         STATUS TEXT DEFAULT 'WORKING'
# #     #     )''')

# #     #     cursor.execute('''CREATE TABLE IF NOT EXISTS Saida (
# #     #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# #     #         HORA_SAI TEXT,
# #     #         STATUS TEXT DEFAULT 'EXIT'
# #     #     )''')

# #     #     conn.commit()
# #     #     conn.close()


# import tkinter as tk


# def Point(center_frame):
#     # Limpa o conteúdo atual do frame central
#     for widget in center_frame.winfo_children():
#         widget.destroy()

#     # ---------- Conteúdo do quadro branco ----------
#     nome_lbl = tk.Label(center_frame, text="José Araudo Dos Santos",
#                         font=("Arial", 20), bg="white", fg="black")
#     nome_lbl.pack(padx=10)

#     matricula_lbl = tk.Label(center_frame, text="MATRICULA: 85b690",
#                               font=("Arial", 10), bg="white", fg="black")
#     matricula_lbl.pack(padx=10)

#     codigo_lbl = tk.Label(center_frame, text="CÓDIGO",
#                            font=("Arial", 14, "bold"), bg="white", fg="black")
#     codigo_lbl.pack(padx=10, pady=10)

#     codigo_ety = tk.Entry(center_frame, font=("Arial", 20, "bold"),
#                            bg="#f0f0f0", fg="black", width=15, justify="center")
#     codigo_ety.pack(pady=20)

#     # Footer frame
#     footer_frame = tk.Frame(center_frame, bg="white")
#     footer_frame.pack(fill="both", padx=0, pady=10)

#     Regis_Entrada_btn = tk.Button(center_frame, text="Registrar \nEntrada",
#                                   font=("Arial", 14), bg="#0300A7",
#                                   fg="white", width=20, height=2)
#     Regis_Entrada_btn.pack(pady=10)


# if __name__ == "__main__": 
#     root = tk.Tk()
#     root.title("Cadastro de Funcionário")
#     root.geometry("800x400")
#     root.configure(bg='#FFFFFF')
#     app = Point(root)
#     root.mainloop()


import tkinter as tk
import sqlite3
import os
from datetime import datetime


DB_DIR = r"C:\Users\998096\Documents\python\PROJETO_TURMA_RH_SENAC\DATA"
DB_PATH = os.path.join(DB_DIR, 'REGISTER_POINTS.db')


class Point:

    def __init__(self, master):
        self.master = master
        self.master.configure(bg="white")

        self.data_hoje = datetime.now().strftime('%Y-%m-%d')

        self.titulo = tk.Label(
            master, text="STATUS DO DIA", font=("Arial", 20, "bold"), bg="white"
        )
        self.titulo.pack(pady=10)

        self.frame_info = tk.Frame(master, bg="white")
        self.frame_info.pack(pady=10)

        self.label_total = tk.Label(self.frame_info, text="", bg="white", font=("Arial", 12))
        self.label_total.grid(row=0, column=0, padx=20)

        self.label_registrados = tk.Label(self.frame_info, text="", bg="white", fg="green", font=("Arial", 12))
        self.label_registrados.grid(row=0, column=1, padx=20)

        self.label_pendentes = tk.Label(self.frame_info, text="", bg="white", fg="red", font=("Arial", 12))
        self.label_pendentes.grid(row=0, column=2, padx=20)

        self.frame_listas = tk.Frame(master, bg="white")
        self.frame_listas.pack(pady=10, fill="both", expand=True)

        # Listas
        self.frame_left = tk.Frame(self.frame_listas, bg="#f0f0f0", bd=2, relief="groove")
        self.frame_left.pack(side="left", fill="both", expand=True, padx=10, pady=5)

        self.frame_right = tk.Frame(self.frame_listas, bg="#f0f0f0", bd=2, relief="groove")
        self.frame_right.pack(side="left", fill="both", expand=True, padx=10, pady=5)

        tk.Label(
            self.frame_left, text="✅ Já Registraram Hoje", bg="#f0f0f0",
            font=("Arial", 14, "bold")
        ).pack(pady=5)

        self.lista_registrados = tk.Listbox(self.frame_left, width=40, height=20)
        self.lista_registrados.pack(padx=10, pady=10, fill="both", expand=True)

        tk.Label(
            self.frame_right, text="❌ Não Registraram Hoje", bg="#f0f0f0",
            font=("Arial", 14, "bold")
        ).pack(pady=5)

        self.lista_pendentes = tk.Listbox(self.frame_right, width=40, height=20)
        self.lista_pendentes.pack(padx=10, pady=10, fill="both", expand=True)

        # Atualiza os dados
        self.carregar_dados()

    def carregar_dados(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Buscar todos os colaboradores
        cursor.execute("SELECT id, Nome, RA FROM Colaborador")
        colaboradores = cursor.fetchall()

        total = len(colaboradores)
        registrados = []
        pendentes = []

        for colaborador in colaboradores:
            colaborador_id, nome, ra = colaborador

            cursor.execute('''
                SELECT COUNT(*) FROM RegistroPonto
                WHERE id_funcionario = ? AND data = ?
            ''', (colaborador_id, self.data_hoje))

            resultado = cursor.fetchone()
            if resultado[0] > 0:
                registrados.append(f"{nome} | RA: {ra}")
            else:
                pendentes.append(f"{nome} | RA: {ra}")

        conn.close()

        # Atualiza listas
        self.lista_registrados.delete(0, tk.END)
        self.lista_pendentes.delete(0, tk.END)

        for nome in registrados:
            self.lista_registrados.insert(tk.END, nome)

        for nome in pendentes:
            self.lista_pendentes.insert(tk.END, nome)

        # Atualiza contagens
        self.label_total.config(text=f"👥 Total: {total}")
        self.label_registrados.config(text=f"✅ Registraram: {len(registrados)}")
        self.label_pendentes.config(text=f"❌ Pendentes: {len(pendentes)}")


if __name__ == "__main__":
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Criar tabela de colaboradores
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

    # Criar tabela de registro de ponto
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
    root.title("Registro de Ponto")
    root.geometry("800x600")
    root.mainloop()