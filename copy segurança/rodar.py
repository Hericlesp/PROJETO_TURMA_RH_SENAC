# import tkinter as tk
# import random
# import string

# # Função para abrir a janela de gerar código
# def abrir_gerador_codigo():
#     def gerar_codigo():
#         codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
#         codigo_var.set(codigo)

#     def copiar_codigo():
#         janela.clipboard_clear()
#         janela.clipboard_append(codigo_var.get())

#     janela = tk.Toplevel()
#     janela.title("Gerar Código de 6 Dígitos")
#     janela.geometry("350x200")
#     janela.configure(bg='white')
#     janela.resizable(False, False)

#     tk.Label(janela, text="Código Gerado:", font=("Arial", 14, "bold"), bg="white").pack(pady=10)
#     codigo_var = tk.StringVar()
#     codigo_entry = tk.Entry(janela, textvariable=codigo_var, font=("Arial", 20, "bold"),
#                             bg="#f0f0f0", fg="black", width=10, justify="center")
#     codigo_entry.pack(pady=10)

#     btn_gerar = tk.Button(janela, text="Gerar Código", font=("Arial", 14), bg="#007ACC", fg="white",
#                           command=gerar_codigo, width=15)
#     btn_gerar.pack(pady=5)

#     btn_copiar = tk.Button(janela, text="Copiar Código", font=("Arial", 14), bg="#0300A7", fg="white",
#                            command=copiar_codigo, width=15)
#     btn_copiar.pack(pady=5)


# # Exemplo simplificado de menu lateral com o botão adicionado
# class SistemaPonto:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Sistema de Registro de Ponto - ADMIN")
#         self.root.geometry("1000x600")
#         self.root.minsize(800, 600)
#         self.root.configure(bg="white")
#         self.criar_widgets()

#     def criar_widgets(self):
#         self.menu_frame = tk.Frame(self.root, bg="#d9d9d9", width=150)
#         self.menu_frame.pack(fill="y", side="left")

#         btn_gerar_codigo = tk.Button(
#             self.menu_frame, text="🔑 | Gerar Código", bg="#f0f0f0", width=15,
#             command=abrir_gerador_codigo
#         )
#         btn_gerar_codigo.pack(pady=10)

#         btn_status_dia = tk.Button(
#             self.menu_frame, text="📋 | Status do Dia", bg="#f0f0f0", width=15,
#             # comando da sua função para abrir status do dia
#             command=lambda: print("Abrir Status do Dia")
#         )
#         btn_status_dia.pack(pady=10)

#         # ... outros botões do menu aqui

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = SistemaPonto(root)
#     root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


class RegistroFuncionario:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Funcionário")
        self.master.geometry("700x500")
        self.master.configure(bg='#FFFFFF')

        self.conectar_banco()
        self.criar_tabela()

        self.dados_funcionario()

    def conectar_banco(self):
        self.conn = sqlite3.connect(r'C:\Users\998096\Documents\python\tkinter\DATA\funcionarios.db')
        self.cursor = self.conn.cursor()

    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS funcionarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                matricula TEXT,
                contato TEXT,
                idade INTEGER,
                data_nascimento TEXT,
                cpf TEXT,
                rg TEXT,
                contratacao TEXT,
                cargo TEXT,
                salario REAL,
                data_admissao TEXT,
                ativo TEXT
            )
        ''')
        self.conn.commit()

    def dados_funcionario(self):
        # Frame do destaque
        frame_destaque = tk.Frame(self.master, bg='#00008B')
        frame_destaque.grid(row=0, column=0, sticky='ew')
        self.master.grid_columnconfigure(0, weight=1)

        label_principal = tk.Label(frame_destaque, text='CADASTRAR FUNCIONÁRIO',
                                   fg="#FFFFFF", bg="#00008B", font=("Arial", 14, "bold"))
        label_principal.pack(anchor='center')

        # Frame principal
        frame_cadastro = tk.Frame(self.master, bg='#FFFFFF')
        frame_cadastro.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
        frame_cadastro.grid_columnconfigure(1, weight=1)

        # Campos
        self.campos = {}

        labels = [
            ('Nome:', 60), ('Matrícula:', 40), ('Contato:', 40),
            ('Idade:', 7), ('Data de nascimento:', 25), ('CPF:', 40),
            ('RG:', 40), ('Cargo:', 60), ('Salário:', 10),
            ('Data de admissão:', 40)
        ]

        for idx, (text, width) in enumerate(labels):
            label = tk.Label(frame_cadastro, text=text, fg='#000000', bg='#FFFFFF', font=('Arial', 10))
            label.grid(row=idx, column=0, sticky='w')
            entry = tk.Entry(frame_cadastro, width=width, font=('Arial', 10), relief='solid')
            entry.grid(row=idx, column=1, sticky='w')
            self.campos[text[:-1].lower()] = entry

        # Contratação
        label_contratacao = tk.Label(frame_cadastro, text='Contratação:', fg='#000000', bg='#FFFFFF', font=('Arial', 10))
        label_contratacao.grid(row=10, column=0, sticky='w')
        self.combo_contratacao = ttk.Combobox(frame_cadastro, values=['Fixa', 'Horista'], width=7, font=('Arial', 10))
        self.combo_contratacao.grid(row=10, column=1, sticky='w')

        # Ativo
        label_ativo = tk.Label(frame_cadastro, text='Funcionário Ativo:', fg='#000000', bg='#FFFFFF', font=('Arial', 10))
        label_ativo.grid(row=11, column=0, sticky='w')
        self.combo_ativo = ttk.Combobox(frame_cadastro, values=['Sim', 'Não'], width=5, font=('Arial', 10))
        self.combo_ativo.grid(row=11, column=1, sticky='w')

        # Botões
        botao_salvar = tk.Button(frame_cadastro, text='SALVAR', font=('Arial', 12, 'bold'),
                                 bg='#00008B', fg='#FFFFFF', width=12, command=self.salvar_dados)
        botao_salvar.grid(row=12, column=0, pady=10, sticky="w")

        botao_novo = tk.Button(frame_cadastro, text='NOVO CADASTRO', font=('Arial', 12, 'bold'),
                               bg='#00008B', fg='#FFFFFF', width=15, command=self.limpar_campos)
        botao_novo.grid(row=12, column=1, pady=5, sticky="e")

    def salvar_dados(self):
        confirmar = messagebox.askyesno("Confirmação", "Deseja salvar os dados?")
        if confirmar:
            try:
                self.cursor.execute('''
                    INSERT INTO funcionarios (
                        nome, matricula, contato, idade, data_nascimento,
                        cpf, rg, contratacao, cargo, salario,
                        data_admissao, ativo
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    self.campos['nome'].get(),
                    self.campos['matrícula'].get(),
                    self.campos['contato'].get(),
                    self.campos['idade'].get(),
                    self.campos['data de nascimento'].get(),
                    self.campos['cpf'].get(),
                    self.campos['rg'].get(),
                    self.combo_contratacao.get(),
                    self.campos['cargo'].get(),
                    self.campos['salário'].get(),
                    self.campos['data de admissão'].get(),
                    self.combo_ativo.get()
                ))
                self.conn.commit()
                messagebox.showinfo("Salvo", "Dados salvos com sucesso!")
                self.limpar_campos()
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
        else:
            messagebox.showwarning("Cancelado", "O salvamento foi cancelado.")

    def limpar_campos(self):
        for campo in self.campos.values():
            campo.delete(0, tk.END)
        self.combo_contratacao.set('')
        self.combo_ativo.set('')


if __name__ == "__main__":
    root = tk.Tk()
    app = RegistroFuncionario(root)
    root.mainloop()
