# import tkinter as tk
# import sqlite3
# import os

# # Importando os módulos internos
# import registro_funcionario
# import help
# import POINT_registrar as point
#from criar_banco import criar_banco_e_tabela


# # Caminho para o banco de dados
# DB_DIR = r"C:\Users\998096\Documents\python\PROJETO_TURMA_RH_SENAC\DATA"
# DB_PATH = os.path.join(DB_DIR, 'REGISTER_POINTS.db')


# class SistemaPonto:

#     @staticmethod
#     def criar_banco():
#         if not os.path.exists(DB_DIR):
#             os.makedirs(DB_DIR)

#         conn = sqlite3.connect(DB_PATH)
#         cursor = conn.cursor()

#         cursor.execute('''CREATE TABLE IF NOT EXISTS Colaborador (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             RA INT UNIQUE,
#             Nome TEXT,
#             Setor TEXT,
#             Email TEXT,
#             Celular INT
#         )''')

#         cursor.execute('''CREATE TABLE IF NOT EXISTS Entrada (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             HORA_ENT TEXT,
#             STATUS TEXT DEFAULT 'WORKING'
#         )''')

#         cursor.execute('''CREATE TABLE IF NOT EXISTS Saida (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             HORA_SAI TEXT,
#             STATUS TEXT DEFAULT 'EXIT'
#         )''')

#         conn.commit()
#         conn.close()

#     def __init__(self, root):
#         self.root = root
#         self.root.title("Registro de ponto")
#         self.root.geometry("1000x600")
#         self.root.minsize(800, 600)
#         self.root.configure(bg="white")

#         self.criar_widgets()

#     def criar_widgets(self):
#         # Barra superior
#         self.top_frame = tk.Frame(self.root, bg="green", height=70)
#         self.top_frame.pack(fill="x", side="top")

#         self.title_lbl = tk.Label(
#             self.top_frame, text="REGISTRO DE PONTO",
#             font=("Arial", 20, "bold"), bg="green", fg="white"
#         )
#         self.title_lbl.pack(padx=10, pady=15)

#         # Frame lateral (Menu)
#         self.menu_frame = tk.Frame(self.root, bg="#d9d9d9", width=150)
#         self.menu_frame.pack(fill="y", side="left")

#         # Botões do menu lateral
#         btn_cadastro = tk.Button(
#             self.menu_frame, text="✏️ | Cadastro", bg="#f0f0f0", width=15,
#             command=self.abrir_cadastro
#         )
#         btn_cadastro.pack(pady=10)

#         btn_registrar = tk.Button(
#             self.menu_frame, text="⚪ | Registrar\nPonto", bg="#f0f0f0", width=15,
#             command=self.abrir_ponto
#         )
#         btn_registrar.pack(pady=10)

#         # btn_home = tk.Button(
#         #     self.menu_frame, text="🛟 | Help", bg="#f0f0f0", width=15,
#         #     command=self.abrir_help
#         # )
        
#         btn_home = tk.Button(
#         self.menu_frame,
#         text="🛟 | Help",
#         bg="#f0f0f0",
#         width=15,
#         command=lambda: help.infohelp(self.center_frame)
#         )
#         btn_home.pack(pady=10)

#         btn_home.pack(pady=10)

#         btn_sair = tk.Button(
#             self.menu_frame, text="🚪 | Sair", bg="#f0f0f0", width=15,
#             command=self.root.quit
#         )
#         btn_sair.pack(pady=10)

#         # Frame do centro (Conteúdo dinâmico)
#         self.center_frame = tk.Frame(self.root, bg="white")
#         self.center_frame.pack(fill="both", side="left", expand=True, padx=25, pady=15)

#         # Conteúdo inicial (opcional)
#         self.abrir_home()

#     # ✅ Função para limpar o conteúdo do center_frame
#     def limpar_center(self):
#         for widget in self.center_frame.winfo_children():
#             widget.destroy()

#     # ✅ Funções de navegação
#     def abrir_cadastro(self):
#         self.limpar_center()
#         registro_funcionario.RegistroFuncionario(self.center_frame)

#     def abrir_ponto(self):
#         self.limpar_center()
#         point.Point(self.center_frame)

#     def abrir_help(self):
#         self.limpar_center()
#         help.infohelp(self.center_frame)

#     def abrir_home(self):
#         self.limpar_center()
#         tk.Label(
#             self.center_frame, text="Bem-vindo ao Sistema de Registro de Ponto!",
#             font=("Arial", 18), bg="white"
#         ).pack(pady=50)


#     def run(self):
#         self.root.mainloop()


# # Programa principal
# if __name__ == "__main__":
#     SistemaPonto.criar_banco()
#     root = tk.Tk()
#     app = SistemaPonto(root)
#     app.run()



import tkinter as tk
import sqlite3
import os

# Importando os módulos internos
import registro_funcionario
import help
import POINT_registrar as point
import gerar_codigo


# 📂 Caminho para o banco de dados
DB_DIR = r"C:\Users\998096\Documents\python\PROJETO_TURMA_RH_SENAC\DATA"
DB_PATH = os.path.join(DB_DIR, 'REGISTER_POINTS.db')


class SistemaPonto:

    @staticmethod
    def criar_banco():
        # 📦 Cria a pasta do banco se não existir
        if not os.path.exists(DB_DIR):
            os.makedirs(DB_DIR)

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # ✅ Tabela de colaboradores
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

        # ✅ Tabela de registros de ponto
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
        print('🗄️ Banco de dados verificado/criado com sucesso!')

    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Registro de Ponto - ADMIN")
        self.root.geometry("1000x600")
        self.root.minsize(800, 600)
        self.root.configure(bg="white")

        self.criar_widgets()

    def criar_widgets(self):
        # 🎨 Barra superior
        self.top_frame = tk.Frame(self.root, bg="green", height=70)
        self.top_frame.pack(fill="x", side="top")

        self.title_lbl = tk.Label(
            self.top_frame, text="REGISTRO DE PONTO - ADMIN",
            font=("Arial", 20, "bold"), bg="green", fg="white"
        )
        self.title_lbl.pack(padx=10, pady=15)

        # 📑 Menu lateral
        self.menu_frame = tk.Frame(self.root, bg="#d9d9d9", width=150)
        self.menu_frame.pack(fill="y", side="left")

        # 🔘 Botões do menu lateral
        btn_cadastro = tk.Button(
            self.menu_frame, text="✏️ | Cadastro", bg="#f0f0f0", width=15,
            command=self.abrir_cadastro
        )
        btn_cadastro.pack(pady=10)
        
        btn_gerar = tk.Button(self.menu_frame, text="Gerar Código", bg="#f0f0f0", command=lambda:gerar_codigo.SistemaPonto, width=15)
        btn_gerar.pack(pady=10)

        btn_registrar = tk.Button(
            self.menu_frame, text="📋 | Status do Dia", bg="#f0f0f0", width=15,
            command=self.abrir_ponto
        )
        btn_registrar.pack(pady=10)

        btn_help = tk.Button(
            self.menu_frame,
            text="🛟 | Help",
            bg="#f0f0f0",
            width=15,
            command=lambda: help.infohelp(self.center_frame)
        )
        btn_help.pack(pady=10)

        btn_sair = tk.Button(
            self.menu_frame, text="🚪 | Sair", bg="#f0f0f0", width=15,
            command=self.root.quit
        )
        btn_sair.pack(pady=10)

        # 📄 Área de conteúdo dinâmico
        self.center_frame = tk.Frame(self.root, bg="white")
        self.center_frame.pack(fill="both", side="left", expand=True, padx=25, pady=15)

        # Conteúdo inicial
        self.abrir_home()

    def limpar_center(self):
        for widget in self.center_frame.winfo_children():
            widget.destroy()

    def abrir_cadastro(self):
        self.limpar_center()
        registro_funcionario.RegistroFuncionario(self.center_frame)

    def abrir_ponto(self):
        self.limpar_center()
        point.Point(self.center_frame)

    def abrir_home(self):
        self.limpar_center()
        tk.Label(
            self.center_frame, text="Bem-vindo ao Sistema de Registro de Ponto - ADMIN",
            font=("Arial", 18, "bold"), bg="white"
        ).pack(pady=50)

    def run(self):
        self.root.mainloop()


# 🚀 Programa principal
if __name__ == "__main__":
    SistemaPonto.criar_banco()  # 🗄️ Garante que o banco e as tabelas existam
    root = tk.Tk()
    app = SistemaPonto(root)
    app.run()
