# # # # import tkinter as tk
# # # # from tkinter import *
# # # # from tkinter import ttk
# # # # import datetime as dt



# # # # class SistemaPonto:
# # # #     def __init__(self, root):
# # # #         self.root = root
# # # #         self.root.title("Registro de ponto")
# # # #         self.root.geometry("450x450")
# # # #         self.root.minsize(450, 450)
# # # #         self.root.resizable(False, True)
# # # #         self.root.configure(bg="white")
# # # #         #self.root.iconbitmap(r'C:\Users\998096\Documents\python\PROJETO_TURMA_RH_SENAC\pin.png')
# # # #         #self.root.iconbitmap(r'C:\Users\Justino\Documents\Hexa\git&github\PROJETO_TURMA_RH_SENAC\pin.png')

# # # #         self.criar_widgets()

# # # #     def criar_widgets(self):
# # # #         # Barra superior
# # # #         self.top_frame = tk.Frame(self.root, bg="#F09001", width=900, height=100)
# # # #         self.top_frame.pack(fill="x", side="top", padx=0, pady=0)

# # # #         self.title_lbl = tk.Label(self.top_frame, text="Ponto Eletrônico", font=("Arial", 20,"bold"), bg="#F09001", fg="black")
# # # #         self.title_lbl.pack(padx=10, pady=10)


# # # #         #frame do centro
# # # #         self.center_frame = tk.Frame(self.root, bg="white", width=900, height=300)
# # # #         self.center_frame.pack(fill="both", side="top", padx=0, pady=15)

# # # #         self.nome_lbl = tk.Label(self.center_frame, text="José Araudo Dos Santos", font=("Arial", 28), bg="white", fg="black")
# # # #         self.nome_lbl.pack(padx=10)


# # # #         self.Matricula_lbl = tk.Label(self.center_frame, text=" MATRICULA: 85b690", font=("Arial", 10), bg="white", fg="black")
# # # #         self.Matricula_lbl.pack(padx=10)
        
# # # #         self.codigo_lbl = tk.Label(self.center_frame, text="CÓDIGO", font=("Arial", 14,"bold"), bg="white", fg="black")
# # # #         self.codigo_lbl.pack(padx=10, pady=10)

# # # #         codigo_ety = tk.Entry(self.center_frame, font=("Arial", 20, "bold"), bg="#f0f0f0", fg="black", width=15, justify="center") 
# # # #         codigo_ety.pack(pady=20)



# # # #         #footer frame

# # # #         self.footer_frame = tk.Frame(self.root, bg="white", width=900, height=100)
# # # #         self.footer_frame.pack(fill="both", padx=0, pady=10)

# # # #         Regis_Entrada_btn = tk.Button(self.footer_frame, text="Registrar \n Entrada", font=("Arial", 14), bg="#0300A7", fg="white", width=20, height=2)
# # # #         Regis_Entrada_btn.pack(pady=10)


# # # #     def run(self):
# # # #         self.root.mainloop()

# # # # # Programa principal
# # # # if __name__ == "__main__":
# # # #     root = tk.Tk()
# # # #     point = SistemaPonto(root)
# # # #     point.run()




# # # # ''' PRECISAMOS DE:
# # # # * TABELA COM DADOS INDIVIDUAIS DOS FUNCIONARIOS:
# # # #       HORARIO DE ENTRADA
# # # #       HORARIO DE SAIDA
# # # #       HORARIO DE ALMOÇO
      
# # # # * REGISTRO DE PONTO
# # # # * REGISTRO DE FALTA
# # # # * REGISTRO DE ATESTADO
# # # # * REGISTRO DE FERIADO
# # # # '''

# # # import tkinter as tk
# # # from tkinter import messagebox
# # # import sqlite3
# # # import os
# # # from datetime import datetime


# # # # 📂 Caminho do banco
# # # DB_DIR = r"C:\Users\998096\Documents\python\PROJETO_TURMA_RH_SENAC\DATA"
# # # DB_PATH = os.path.join(DB_DIR, 'REGISTER_POINTS.db')


# # # class SistemaPonto:
# # #     def __init__(self, root):
# # #         self.root = root
# # #         self.root.title("Registro de Ponto")
# # #         self.root.geometry("450x600")
# # #         self.root.minsize(450, 600)
# # #         self.root.resizable(False, True)
# # #         self.root.configure(bg="white")
# # #         #self.root.iconbitmap(r'CAMINHO_DO_ICONE\pin.png')  # Se quiser usar ícone

# # #         self.nome = tk.StringVar()
# # #         self.ra = tk.StringVar()

# # #         self.criar_widgets()

# # #     def criar_widgets(self):
# # #         # 🔶 Barra superior
# # #         self.top_frame = tk.Frame(self.root, bg="#F09001", height=100)
# # #         self.top_frame.pack(fill="x", side="top")

# # #         self.title_lbl = tk.Label(
# # #             self.top_frame, text="Ponto Eletrônico",
# # #             font=("Arial", 20, "bold"), bg="#F09001", fg="black"
# # #         )
# # #         self.title_lbl.pack(pady=15)

# # #         # 🔲 Centro
# # #         self.center_frame = tk.Frame(self.root, bg="white")
# # #         self.center_frame.pack(fill="both", side="top", pady=15)

# # #         self.nome_lbl = tk.Label(
# # #             self.center_frame, text="", font=("Arial", 20),
# # #             bg="white", fg="black"
# # #         )
# # #         self.nome_lbl.pack(pady=5)

# # #         self.matricula_lbl = tk.Label(
# # #             self.center_frame, text="", font=("Arial", 10),
# # #             bg="white", fg="black"
# # #         )
# # #         self.matricula_lbl.pack()

# # #         self.codigo_lbl = tk.Label(
# # #             self.center_frame, text="CÓDIGO", font=("Arial", 14, "bold"),
# # #             bg="white", fg="black"
# # #         )
# # #         self.codigo_lbl.pack(pady=(10, 0))

# # #         self.codigo_entry = tk.Entry(
# # #             self.center_frame, font=("Arial", 20, "bold"),
# # #             bg="#f0f0f0", fg="black", width=15, justify="center"
# # #         )
# # #         self.codigo_entry.pack(pady=10)

# # #         # 🔘 Botões no rodapé
# # #         self.footer_frame = tk.Frame(self.root, bg="white")
# # #         self.footer_frame.pack(fill="both", pady=10)

# # #         btn_entrada = tk.Button(
# # #             self.footer_frame, text="Registrar\nEntrada",
# # #             font=("Arial", 14), bg="#0300A7", fg="white",
# # #             width=20, height=2, command=lambda: self.registrar_ponto("Entrada")
# # #         )
# # #         btn_entrada.pack(pady=5)

# # #         btn_saida = tk.Button(
# # #             self.footer_frame, text="Registrar\nSaída",
# # #             font=("Arial", 14), bg="#0300A7", fg="white",
# # #             width=20, height=2, command=lambda: self.registrar_ponto("Saída")
# # #         )
# # #         btn_saida.pack(pady=5)

# # #         btn_almoco = tk.Button(
# # #             self.footer_frame, text="Registrar\nAlmoço",
# # #             font=("Arial", 14), bg="#0300A7", fg="white",
# # #             width=20, height=2, command=lambda: self.registrar_ponto("Almoço")
# # #         )
# # #         btn_almoco.pack(pady=5)

# # #         btn_retorno = tk.Button(
# # #             self.footer_frame, text="Registrar\nRetorno",
# # #             font=("Arial", 14), bg="#0300A7", fg="white",
# # #             width=20, height=2, command=lambda: self.registrar_ponto("Retorno")
# # #         )
# # #         btn_retorno.pack(pady=5)

# # #         # 🔍 Inicialmente limpa os dados
# # #         self.atualizar_dados_funcionario("", "")

# # #     def conectar(self):
# # #         return sqlite3.connect(DB_PATH)

# # #     def buscar_funcionario_por_codigo(self, codigo):
# # #         conn = self.conectar()
# # #         cursor = conn.cursor()
# # #         cursor.execute(
# # #             "SELECT id, Nome, RA FROM Colaborador WHERE Codigo=?",
# # #             (codigo,)
# # #         )
# # #         resultado = cursor.fetchone()
# # #         conn.close()
# # #         return resultado

# # #     def atualizar_dados_funcionario(self, nome, ra):
# # #         self.nome.set(nome)
# # #         self.ra.set(ra)
# # #         self.nome_lbl.config(text=nome.upper() if nome else "")
# # #         self.matricula_lbl.config(text=f"MATRICULA: {ra}" if ra else "")

# # #     def registrar_ponto(self, tipo):
# # #         codigo = self.codigo_entry.get().strip()

# # #         if not codigo:
# # #             messagebox.showwarning("Atenção", "Informe seu CÓDIGO para registrar o ponto.")
# # #             return

# # #         funcionario = self.buscar_funcionario_por_codigo(codigo)

# # #         if not funcionario:
# # #             messagebox.showerror("Erro", "Código inválido. Tente novamente.")
# # #             self.atualizar_dados_funcionario("", "")
# # #             return

# # #         id_funcionario, nome, ra = funcionario

# # #         self.atualizar_dados_funcionario(nome, ra)

# # #         data_atual = datetime.now().strftime("%Y-%m-%d")
# # #         hora_atual = datetime.now().strftime("%H:%M:%S")

# # #         conn = self.conectar()
# # #         cursor = conn.cursor()
# # #         cursor.execute('''
# # #             INSERT INTO RegistroPonto (id_funcionario, data, hora, tipo)
# # #             VALUES (?, ?, ?, ?)
# # #         ''', (id_funcionario, data_atual, hora_atual, tipo))
# # #         conn.commit()
# # #         conn.close()

# # #         messagebox.showinfo(
# # #             "Sucesso",
# # #             f"{tipo} registrado com sucesso às {hora_atual}.\n\nFuncionário: {nome}"
# # #         )

# # #         self.codigo_entry.delete(0, tk.END)


# # #     def run(self):
# # #         self.root.mainloop()


# # # # ▶️ Executar o programa
# # # if __name__ == "__main__":
# # #     root = tk.Tk()
# # #     app = SistemaPonto(root)
# # #     app.run()

# # import tkinter as tk
# # from tkinter import ttk, messagebox
# # import datetime as dt
# # import sqlite3
# # import os


# # # Caminho do banco de dados
# # DB_DIR = r"C:\Users\998096\Documents\python\PROJETO_TURMA_RH_SENAC\DATA"
# # DB_PATH = os.path.join(DB_DIR, 'REGISTER_POINTS.db')


# # class SistemaPonto:
# #     def __init__(self, root):
# #         self.root = root
# #         self.root.title("Registro de ponto")
# #         self.root.geometry("450x500")
# #         self.root.minsize(450, 500)
# #         self.root.resizable(False, False)
# #         self.root.configure(bg="white")

# #         self.criar_widgets()

# #     def criar_widgets(self):
# #         # 🔶 Barra superior
# #         self.top_frame = tk.Frame(self.root, bg="#F09001", width=450, height=100)
# #         self.top_frame.pack(fill="x", side="top")

# #         self.title_lbl = tk.Label(
# #             self.top_frame,
# #             text="Ponto Eletrônico",
# #             font=("Arial", 20, "bold"),
# #             bg="#F09001",
# #             fg="black"
# #         )
# #         self.title_lbl.pack(padx=10, pady=10)

# #         # 🔲 Frame central
# #         self.center_frame = tk.Frame(self.root, bg="white")
# #         self.center_frame.pack(fill="both", side="top", pady=15)

# #         # 🔤 Nome do funcionário
# #         self.nome_lbl = tk.Label(
# #             self.center_frame,
# #             text="José Araudo Dos Santos",
# #             font=("Arial", 20, "bold"),
# #             bg="white",
# #             fg="black"
# #         )
# #         self.nome_lbl.pack(pady=(0, 5))

# #         # 🔢 Matrícula
# #         self.matricula_lbl = tk.Label(
# #             self.center_frame,
# #             text="MATRÍCULA: 85B690",
# #             font=("Arial", 14),
# #             bg="white",
# #             fg="black"
# #         )
# #         self.matricula_lbl.pack(pady=(0, 15))

# #         # 🔑 Código
# #         self.codigo_lbl = tk.Label(
# #             self.center_frame,
# #             text="CÓDIGO",
# #             font=("Arial", 14, "bold"),
# #             bg="white",
# #             fg="black"
# #         )
# #         self.codigo_lbl.pack(pady=(5, 5))

# #         # Campo para inserir código
# #         self.codigo_entry = tk.Entry(
# #             self.center_frame,
# #             font=("Arial", 20, "bold"),
# #             bg="#f0f0f0",
# #             fg="black",
# #             width=15,
# #             justify="center"
# #         )
# #         self.codigo_entry.pack(pady=10)

# #         # 🔽 Tipo de registro (Combobox)
# #         self.tipo_lbl = tk.Label(
# #             self.center_frame,
# #             text="Selecione o Tipo de Registro:",
# #             font=("Arial", 12),
# #             bg="white",
# #             fg="black"
# #         )
# #         self.tipo_lbl.pack(pady=(15, 5))

# #         self.tipo_combobox = ttk.Combobox(
# #             self.center_frame,
# #             font=("Arial", 12),
# #             width=25,
# #             state="readonly",
# #             values=[
# #                 "Entrada",
# #                 "Saída para Almoço",
# #                 "Retorno do Almoço",
# #                 "Saída"
# #             ]
# #         )
# #         self.tipo_combobox.set("Entrada")  # valor padrão
# #         self.tipo_combobox.pack(pady=5)

# #         # 🔘 Footer (Botão)
# #         self.footer_frame = tk.Frame(self.root, bg="white")
# #         self.footer_frame.pack(fill="both", padx=0, pady=10)

# #         # Botão Registrar
# #         self.registrar_btn = tk.Button(
# #             self.footer_frame,
# #             text="Registrar",
# #             font=("Arial", 14),
# #             bg="#0300A7",
# #             fg="white",
# #             width=20,
# #             height=2,
# #             command=self.registrar_ponto
# #         )
# #         self.registrar_btn.pack(pady=10)

# #     def registrar_ponto(self):
# #         codigo = self.codigo_entry.get().strip()
# #         tipo = self.tipo_combobox.get()

# #         if codigo == "":
# #             messagebox.showerror("Erro", "Por favor, insira o código.")
# #             return

# #         if tipo == "":
# #             messagebox.showerror("Erro", "Selecione o tipo de registro.")
# #             return

# #         data = dt.datetime.now().strftime('%Y-%m-%d')
# #         hora = dt.datetime.now().strftime('%H:%M:%S')

# #         try:
# #             conn = sqlite3.connect(DB_PATH)
# #             cursor = conn.cursor()

# #             # Verificar se o colaborador existe
# #             cursor.execute("SELECT id, Nome FROM Colaborador WHERE Codigo = ?", (codigo,))
# #             resultado = cursor.fetchone()

# #             if resultado:
# #                 id_funcionario = resultado[0]
# #                 nome_funcionario = resultado[1]

# #                 # Inserir o registro de ponto
# #                 cursor.execute(
# #                     "INSERT INTO RegistroPonto (id_funcionario, data, hora, tipo) VALUES (?, ?, ?, ?)",
# #                     (id_funcionario, data, hora, tipo)
# #                 )
# #                 conn.commit()

# #                 messagebox.showinfo(
# #                     "Ponto Registrado",
# #                     f"{tipo} registrado com sucesso para {nome_funcionario}\n{data} {hora}"
# #                 )
# #                 self.codigo_entry.delete(0, tk.END)

# #             else:
# #                 messagebox.showerror("Erro", "Código não encontrado.")

# #             conn.close()

# #         except Exception as e:
# #             messagebox.showerror("Erro no banco de dados", str(e))

# #     def run(self):
# #         self.root.mainloop()


# # # Programa principal
# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     point = SistemaPonto(root)
# #     point.run()


# import tkinter as tk
# from tkinter import ttk, messagebox
# import sqlite3
# import os
# import datetime as dt


# # 📍 Caminho do banco de dados
# DB_DIR = r"C:\Users\998096\Documents\python\PROJETO_TURMA_RH_SENAC\DATA"
# DB_PATH = os.path.join(DB_DIR, 'REGISTER_POINTS.db')


# class SistemaPonto:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Registro de ponto")
#         self.root.geometry("450x450")
#         self.root.minsize(450, 450)
#         self.root.resizable(False, True)
#         self.root.configure(bg="white")

#         # Variáveis
#         self.nome_var = tk.StringVar()
#         self.ra_var = tk.StringVar()
#         self.codigo_var = tk.StringVar()
#         self.tipo_var = tk.StringVar()

#         self.criar_widgets()

#     def criar_widgets(self):
#         # 🔸 Top Frame
#         self.top_frame = tk.Frame(self.root, bg="#F09001", width=900, height=100)
#         self.top_frame.pack(fill="x", side="top")

#         self.title_lbl = tk.Label(
#             self.top_frame, text="Ponto Eletrônico",
#             font=("Arial", 20, "bold"), bg="#F09001", fg="black"
#         )
#         self.title_lbl.pack(padx=10, pady=10)

#         # 🔸 Center Frame
#         self.center_frame = tk.Frame(self.root, bg="white")
#         self.center_frame.pack(fill="both", side="top", padx=0, pady=15)

#         self.nome_lbl = tk.Label(
#             self.center_frame, textvariable=self.nome_var,
#             font=("Arial", 20, "bold"), bg="white", fg="black"
#         )
#         self.nome_lbl.pack(padx=10)

#         self.matricula_lbl = tk.Label(
#             self.center_frame, textvariable=self.ra_var,
#             font=("Arial", 14), bg="white", fg="black"
#         )
#         self.matricula_lbl.pack(padx=10)

#         tk.Label(
#             self.center_frame, text="CÓDIGO",
#             font=("Arial", 14, "bold"), bg="white", fg="black"
#         ).pack(padx=10, pady=10)

#         self.codigo_ety = tk.Entry(
#             self.center_frame, font=("Arial", 20, "bold"),
#             bg="#f0f0f0", fg="black", width=15, justify="center"
#         )
#         self.codigo_ety.pack(pady=5)

#         buscar_btn = tk.Button(
#             self.center_frame, text="Buscar",
#             font=("Arial", 10), bg="#F09001", fg="black",
#             command=self.buscar_funcionario
#         )
#         buscar_btn.pack(pady=5)

#         tk.Label(
#             self.center_frame, text="Tipo de Registro",
#             font=("Arial", 14), bg="white", fg="black"
#         ).pack(pady=5)

#         self.tipo_cbx = ttk.Combobox(
#             self.center_frame, values=["Entrada", "Almoço", "Retorno", "Saída"],
#             font=("Arial", 12), state="readonly", textvariable=self.tipo_var
#         )
#         self.tipo_cbx.pack(pady=5)
#         self.tipo_cbx.set("Entrada")

#         # 🔸 Footer Frame
#         self.footer_frame = tk.Frame(self.root, bg="white")
#         self.footer_frame.pack(fill="both", pady=10)

#         registrar_btn = tk.Button(
#             self.footer_frame, text="Registrar",
#             font=("Arial", 14), bg="#0300A7", fg="white",
#             width=20, height=2, command=self.registrar_ponto
#         )
#         registrar_btn.pack(pady=10)

#     # 🔍 Buscar informações do funcionário
#     def buscar_funcionario(self):
#         codigo = self.codigo_ety.get().strip()

#         if not codigo:
#             messagebox.showwarning("Aviso", "Digite o código!")
#             return

#         conn = sqlite3.connect(DB_PATH)
#         cursor = conn.cursor()

#         cursor.execute(
#             "SELECT id, Nome, RA FROM Colaborador WHERE Codigo = ?", (codigo,)
#         )
#         resultado = cursor.fetchone()
#         conn.close()

#         if resultado:
#             self.funcionario_id = resultado[0]
#             self.nome_var.set(resultado[1])
#             self.ra_var.set(f"MATRICULA: {resultado[2]}")
#         else:
#             self.funcionario_id = None
#             self.nome_var.set("")
#             self.ra_var.set("")
#             messagebox.showerror("Erro", "Código não encontrado!")

#     # ⏰ Registrar ponto
#     def registrar_ponto(self):
#         if not getattr(self, 'funcionario_id', None):
#             messagebox.showerror("Erro", "Busque um funcionário antes de registrar.")
#             return

#         tipo = self.tipo_var.get()
#         data = dt.datetime.now().strftime('%Y-%m-%d')
#         hora = dt.datetime.now().strftime('%H:%M:%S')

#         conn = sqlite3.connect(DB_PATH)
#         cursor = conn.cursor()

#         cursor.execute(
#             '''
#             INSERT INTO RegistroPonto (id_funcionario, data, hora, tipo)
#             VALUES (?, ?, ?, ?)
#             ''',
#             (self.funcionario_id, data, hora, tipo)
#         )

#         conn.commit()
#         conn.close()

#         messagebox.showinfo("Sucesso", f"{tipo} registrada com sucesso!")

#     def run(self):
#         self.root.mainloop()


# # 🔧 Criar banco de dados se não existir + cadastrar funcionário exemplo
# def criar_banco():
#     if not os.path.exists(DB_DIR):
#         os.makedirs(DB_DIR)

#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()

#     # Tabela de funcionários
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS Colaborador (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             RA INTEGER UNIQUE,
#             Nome TEXT NOT NULL,
#             Setor TEXT,
#             Email TEXT,
#             Celular TEXT,
#             Codigo TEXT NOT NULL
#         )
#     ''')

#     # Tabela de registros de ponto
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS RegistroPonto (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             id_funcionario INTEGER,
#             data TEXT,
#             hora TEXT,
#             tipo TEXT,
#             FOREIGN KEY (id_funcionario) REFERENCES Colaborador(id)
#         )
#     ''')

#     # 🔥 Inserir funcionário exemplo se não existir
#     cursor.execute(
#         "SELECT * FROM Colaborador WHERE RA = ?", (998096,)
#     )
#     if cursor.fetchone() is None:
#         cursor.execute(
#             '''
#             INSERT INTO Colaborador (RA, Nome, Setor, Email, Celular, Codigo)
#             VALUES (?, ?, ?, ?, ?, ?)
#             ''',
#             (
#                 998096,
#                 'Hericles Paulo da Silva Mendes',
#                 'TI',
#                 'hericles@email.com',
#                 '11999999999',
#                 '1234'   # Código para acesso
#             )
#         )
#         print("Funcionário exemplo cadastrado com sucesso!")

#     conn.commit()
#     conn.close()


# # 🚀 Programa principal
# if __name__ == "__main__":
#     criar_banco()
#     root = tk.Tk()
#     app = SistemaPonto(root)
#     app.run()

import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import os
import datetime as dt

DB_DIR = r"C:\Users\998096\Documents\python\PROJETO_TURMA_RH_SENAC\DATA"
DB_PATH = os.path.join(DB_DIR, 'REGISTER_POINTS.db')


class SistemaPonto:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de ponto")
        self.root.geometry("450x450")
        self.root.minsize(450, 450)
        self.root.resizable(False, True)
        self.root.configure(bg="white")

        self.nome_var = tk.StringVar()
        self.ra_var = tk.StringVar()
        self.codigo_var = tk.StringVar()
        self.tipo_var = tk.StringVar()

        self.funcionario_id = None

        self.criar_widgets()
        self.carregar_funcionario_padrao()  # Carrega o funcionário exemplo na inicialização

    def criar_widgets(self):
        self.top_frame = tk.Frame(self.root, bg="#F09001", width=900, height=100)
        self.top_frame.pack(fill="x", side="top")

        self.title_lbl = tk.Label(
            self.top_frame, text="Ponto Eletrônico",
            font=("Arial", 20, "bold"), bg="#F09001", fg="black"
        )
        self.title_lbl.pack(padx=10, pady=10)

        self.center_frame = tk.Frame(self.root, bg="white")
        self.center_frame.pack(fill="both", side="top", padx=0, pady=15)

        self.nome_lbl = tk.Label(
            self.center_frame, textvariable=self.nome_var,
            font=("Arial", 20, "bold"), bg="white", fg="black"
        )
        self.nome_lbl.pack(padx=10)

        self.matricula_lbl = tk.Label(
            self.center_frame, textvariable=self.ra_var,
            font=("Arial", 14), bg="white", fg="black"
        )
        self.matricula_lbl.pack(padx=10)

        tk.Label(
            self.center_frame, text="CÓDIGO",
            font=("Arial", 14, "bold"), bg="white", fg="black"
        ).pack(padx=10, pady=10)

        self.codigo_ety = tk.Entry(
            self.center_frame, font=("Arial", 20, "bold"),
            bg="#f0f0f0", fg="black", width=15, justify="center"
        )
        self.codigo_ety.pack(pady=5)

        buscar_btn = tk.Button(
            self.center_frame, text="Buscar",
            font=("Arial", 10), bg="#F09001", fg="black",
            command=self.buscar_funcionario
        )
        buscar_btn.pack(pady=5)

        tk.Label(
            self.center_frame, text="Tipo de Registro",
            font=("Arial", 14), bg="white", fg="black"
        ).pack(pady=5)

        self.tipo_cbx = ttk.Combobox(
            self.center_frame, values=["Entrada", "Almoço", "Retorno", "Saída"],
            font=("Arial", 12), state="readonly", textvariable=self.tipo_var
        )
        self.tipo_cbx.pack(pady=5)
        self.tipo_cbx.set("Entrada")

        self.footer_frame = tk.Frame(self.root, bg="white")
        self.footer_frame.pack(fill="both", pady=10)

        registrar_btn = tk.Button(
            self.footer_frame, text="Registrar",
            font=("Arial", 14), bg="#0300A7", fg="white",
            width=20, height=2, command=self.registrar_ponto
        )
        registrar_btn.pack(pady=10)

    def carregar_funcionario_padrao(self):
        # Carrega o funcionário com RA=998096 (exemplo) ao iniciar
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT id, Nome, RA FROM Colaborador WHERE RA = ?", (998096,))
        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            self.funcionario_id = resultado[0]
            self.nome_var.set(resultado[1])
            self.ra_var.set(f"MATRICULA: {resultado[2]}")
            self.codigo_ety.delete(0, tk.END)
            self.codigo_ety.insert(0, '1234')  # Código do exemplo

        else:
            self.funcionario_id = None
            self.nome_var.set("")
            self.ra_var.set("")

    def buscar_funcionario(self):
        codigo = self.codigo_ety.get().strip()

        if not codigo:
            messagebox.showwarning("Aviso", "Digite o código!")
            return

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, Nome, RA FROM Colaborador WHERE Codigo = ?", (codigo,)
        )
        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            self.funcionario_id = resultado[0]
            self.nome_var.set(resultado[1])
            self.ra_var.set(f"MATRICULA: {resultado[2]}")
        else:
            self.funcionario_id = None
            self.nome_var.set("")
            self.ra_var.set("")
            messagebox.showerror("Erro", "Código não encontrado!")

    def registrar_ponto(self):
        if not self.funcionario_id:
            messagebox.showerror("Erro", "Busque um funcionário antes de registrar.")
            return

        tipo = self.tipo_var.get()
        data = dt.datetime.now().strftime('%Y-%m-%d')
        hora = dt.datetime.now().strftime('%H:%M:%S')

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute(
            '''
            INSERT INTO RegistroPonto (id_funcionario, data, hora, tipo)
            VALUES (?, ?, ?, ?)
            ''',
            (self.funcionario_id, data, hora, tipo)
        )

        conn.commit()
        conn.close()

        messagebox.showinfo("Sucesso", f"{tipo} registrada com sucesso!")

    def run(self):
        self.root.mainloop()


def criar_banco():
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR)

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

    cursor.execute(
        "SELECT * FROM Colaborador WHERE RA = ?", (998096,)
    )
    if cursor.fetchone() is None:
        cursor.execute(
            '''
            INSERT INTO Colaborador (RA, Nome, Setor, Email, Celular, Codigo)
            VALUES (?, ?, ?, ?, ?, ?)
            ''',
            (
                998096,
                'Hericles Paulo da Silva Mendes',
                'TI',
                'hericles@email.com',
                '11999999999',
                '1234'
            )
        )
        print("Funcionário exemplo cadastrado com sucesso!")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    criar_banco()
    root = tk.Tk()
    app = SistemaPonto(root)
    app.run()
