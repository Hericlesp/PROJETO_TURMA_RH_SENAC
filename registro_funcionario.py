# # # import tkinter as tk
# # # from tkinter import *


# # # class RegistroFuncionario(tk.Toplevel):
# # #     def __init__(self, master=None):
# # #         super().__init__(master)
# # #         self.title("Cadastro de Funcionário")
# # #         self.geometry("800x400")
# # #         self.configure(bg='#FFFFFF')
# # #         self.dados_funcionario()

# # #     def dados_funcionario(self):
# # #         Label(self, text='CADASTRAR FUNCIONÁRIO',
# # #               fg='#000000', bg='#FFFFFF', font=('Arial', 14)).grid(row=0, column=1, columnspan=5, pady=10)

# # #         Label(self, text='Nome do funcionário:',
# # #               fg='#000000', bg='#FFFFFF').grid(row=1, column=0, sticky=W)
# # #         Entry(self, width=80,
# # #               bg='#FFFFFF', fg='#000000').grid(row=1, column=1, columnspan=5, sticky=W)

# # #         Label(self, text='Idade:',
# # #               fg='#000000', bg='#FFFFFF').grid(row=2, column=3, sticky=W)
# # #         Entry(self, width=10,
# # #               bg='#FFFFFF', fg='#000000').grid(row=2, column=4, sticky=W)

# # #         Label(self, text='Data de nascimento:',
# # #               fg='#000000', bg='#FFFFFF').grid(row=2, column=0, sticky=W)
# # #         Entry(self, width=25,
# # #               bg='#FFFFFF', fg='#000000').grid(row=2, column=1, sticky=W)

# # #         Label(self, text='CPF:',
# # #               fg='#000000', bg='#FFFFFF').grid(row=3, column=0, sticky=W)
# # #         Entry(self, width=25,
# # #               bg='#FFFFFF', fg='#000000').grid(row=3, column=1, sticky=W)

# # #         Label(self, text='RG:',
# # #               fg='#000000', bg='#FFFFFF').grid(row=3, column=3, sticky=W)
# # #         Entry(self, width=25,
# # #               bg='#FFFFFF', fg='#000000').grid(row=3, column=4, sticky=W)

# # #         Label(self, text='Contratação:',
# # #               fg='#000000', bg='#FFFFFF').grid(row=4, column=0, sticky=W)

# # #         Label(self, text='Cargo:',
# # #               fg='#000000', bg='#FFFFFF').grid(row=6, column=0, sticky=W)
# # #         Entry(self, width=40,
# # #               bg='#FFFFFF', fg='#000000').grid(row=6, column=1)

# # #         Label(self, text='Salário (se fixo):',
# # #               fg='#000000', bg='#FFFFFF').grid(row=6, column=3, sticky=E)
# # #         Entry(self, width=10,
# # #               bg='#FFFFFF', fg='#000000').grid(row=6, column=4, sticky=W)

# # #         Label(self, text='Salário (se horista):',
# # #               fg='#000000', bg='#FFFFFF').grid(row=6, column=5, sticky=W)
# # #         Entry(self, width=10,
# # #               bg='#FFFFFF', fg='#000000').grid(row=6, column=6, sticky=E)

# # #         Label(self, text='Data de admissão:',
# # #               fg='#000000', bg='#FFFFFF').grid(row=7, column=0, sticky=W)

# # #         Label(self, text='Data de demissão:',
# # #               fg='#000000', bg='#FFFFFF').grid(row=7, column=3, sticky=W)





# # # ''''
# # # ADICIONAR

# # # botao de salvar = que salva os dados dos funcionarios no banco de dados:
# # # sendo:
# # # *tabela funcionarios da empresa
# # # *tabela individual do funcionario

# # # ou tudo lincado po ID

# # # '''



# # import tkinter as tk


# # class RegistroFuncionario:
# #     def __init__(self, master):
# #         self.master = master
# #         self.criar_interface()

# #     def criar_interface(self):
# #         for widget in self.master.winfo_children():
# #             widget.destroy()

# #         titulo = tk.Label(self.master, text='CADASTRAR FUNCIONÁRIO',
# #                           fg='#000000', bg='#FFFFFF', font=('Arial', 18, 'bold'))
# #         titulo.grid(row=0, column=0, columnspan=6, pady=10)

# #         tk.Label(self.master, text='Nome do funcionário:', bg='#FFFFFF').grid(row=1, column=0, sticky='w')
# #         tk.Entry(self.master, width=50, bg='#FFFFFF').grid(row=1, column=1, columnspan=3, sticky='w')

# #         tk.Label(self.master, text='Idade:', bg='#FFFFFF').grid(row=2, column=3, sticky='w')
# #         tk.Entry(self.master, width=10, bg='#FFFFFF').grid(row=2, column=4, sticky='w')

# #         tk.Label(self.master, text='Data de nascimento:', bg='#FFFFFF').grid(row=2, column=0, sticky='w')
# #         tk.Entry(self.master, width=20, bg='#FFFFFF').grid(row=2, column=1, sticky='w')

# #         tk.Label(self.master, text='CPF:', bg='#FFFFFF').grid(row=3, column=0, sticky='w')
# #         tk.Entry(self.master, width=20, bg='#FFFFFF').grid(row=3, column=1, sticky='w')

# #         tk.Label(self.master, text='RG:', bg='#FFFFFF').grid(row=3, column=3, sticky='w')
# #         tk.Entry(self.master, width=20, bg='#FFFFFF').grid(row=3, column=4, sticky='w')

# #         tk.Label(self.master, text='Cargo:', bg='#FFFFFF').grid(row=4, column=0, sticky='w')
# #         tk.Entry(self.master, width=40, bg='#FFFFFF').grid(row=4, column=1, sticky='w')

# #         tk.Label(self.master, text='Salário (fixo):', bg='#FFFFFF').grid(row=4, column=3, sticky='w')
# #         tk.Entry(self.master, width=10, bg='#FFFFFF').grid(row=4, column=4, sticky='w')

# #         tk.Label(self.master, text='Salário (horista):', bg='#FFFFFF').grid(row=4, column=5, sticky='w')
# #         tk.Entry(self.master, width=10, bg='#FFFFFF').grid(row=4, column=6, sticky='w')

# #         tk.Label(self.master, text='Data de admissão:', bg='#FFFFFF').grid(row=5, column=0, sticky='w')
# #         tk.Entry(self.master, width=20, bg='#FFFFFF').grid(row=5, column=1, sticky='w')

# #         tk.Label(self.master, text='Data de demissão:', bg='#FFFFFF').grid(row=5, column=3, sticky='w')
# #         tk.Entry(self.master, width=20, bg='#FFFFFF').grid(row=5, column=4, sticky='w')

# #         # Botão salvar (para implementar função de banco depois)
# #         salvar_btn = tk.Button(self.master, text='Salvar Funcionário',
# #                                bg='#007ACC', fg='white', width=20, height=2)
# #         salvar_btn.grid(row=6, column=0, columnspan=2, pady=20)

# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     root.title("Cadastro de Funcionário")
# #     root.geometry("800x400")
# #     root.configure(bg='#FFFFFF')

# #     app = RegistroFuncionario(root)
# #     root.mainloop()

# #-----------------------------------------------------------------------#

# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox

# class RegistroFuncionario(tk.Toplevel):
#       def __init__(self, master=None):
#         super().__init__(master)
#         self.title("Cadastro de Funcionário")
#         self.geometry("700x450")
#         self.configure(bg='#FFFFFF')
#         self.dados_funcionario()

#       def dados_funcionario(self):
#         # Frame do destaque 
#         frame_destaque = tk.Frame(self, bg='#00008B')
#         frame_destaque.grid(row=0, column=0, sticky='ew')  
#         self.grid_columnconfigure(0, weight=1)

#         label_principal = tk.Label(frame_destaque, text='CADASTRAR FUNCIONÁRIO',
#                                    fg="#FFFFFF", bg="#00008B", font=("Arial", 14, "bold"))
#         label_principal.pack(anchor='center')  


#         # Frame principal 
#         frame_cadastro = tk.Frame(self, bg='#FFFFFF')
#         frame_cadastro.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
#         frame_cadastro.grid_columnconfigure(1, weight=1)

#         label_nome = tk.Label(frame_cadastro, text='Nome:', fg='#000000', bg='#FFFFFF', font=('Arial', 10))
#         label_nome.grid(row=0, column=0, sticky='w')
#         entry_nome = tk.Entry(frame_cadastro, width=60, font=('Arial', 10), relief='solid')
#         entry_nome.grid(row=0, column=1, sticky='w')

#         label_matricula = tk.Label(frame_cadastro, text='N° de matrícula:', fg='#000000', bg='#FFFFFF', font=('Arial', 10))
#         label_matricula.grid(row=1, column=0, sticky='w')
#         entry_matricula = tk.Entry(frame_cadastro, width=40, font=('Arial', 10), relief='solid')
#         entry_matricula.grid(row=1, column=1, sticky='w')

#         label_id = tk.Label(frame_cadastro, text='ID:', fg='#000000', bg='#FFFFFF', font=('Arial', 10))
#         label_id.grid(row=2, column=0, sticky='w')
#         entry_id = tk.Entry(frame_cadastro, width=40, font=('Arial', 10), relief='solid')
#         entry_id.grid(row=2, column=1, sticky='w')

#         label_contato = tk.Label(frame_cadastro, text='Contato:', fg='#000000', bg='#FFFFFF', font=('Arial', 10))
#         label_contato.grid(row=3, column=0, sticky='w')
#         entry_contato = tk.Entry(frame_cadastro, width=40, font=('Arial', 10), relief='solid')
#         entry_contato.grid(row=3, column=1, sticky='w')

#         label_idade = tk.Label(frame_cadastro, text='Idade:', fg='#000000', bg='#FFFFFF', font=('Arial', 10))
#         label_idade.grid(row=4, column=0, sticky='w')
#         entry_idade = tk.Entry(frame_cadastro, width=7, font=('Arial', 10), relief='solid')
#         entry_idade.grid(row=4, column=1, sticky='w')

#         label_data_nascimento = tk.Label(frame_cadastro, text='Data de nascimento:', fg='#000000', bg='#FFFFFF', font=('Arial', 10))
#         label_data_nascimento.grid(row=5, column=0, sticky='w')
#         entry_data_nascimento = tk.Entry(frame_cadastro, width=25, font=('Arial', 10), relief='solid')
#         entry_data_nascimento.grid(row=5, column=1, sticky='w')

#         label_cpf = tk.Label(frame_cadastro, text='CPF:', fg='#000000', bg='#FFFFFF', font=('Arial', 10))
#         label_cpf.grid(row=6, column=0, sticky='w')
#         entry_cpf = tk.Entry(frame_cadastro, width=40, font=('Arial', 10), relief='solid')
#         entry_cpf.grid(row=6, column=1, sticky='w')

#         label_rg = tk.Label(frame_cadastro, text='RG:', fg='#000000', bg='#FFFFFF', font=('Arial', 10))
#         label_rg.grid(row=7, column=0, sticky='w')
#         entry_rg = tk.Entry(frame_cadastro, width=40, font=('Arial', 10), relief='solid')
#         entry_rg.grid(row=7, column=1, sticky='w')

#         label_contratacao = tk.Label(frame_cadastro, text='Contratação:', fg='#000000', bg='#FFFFFF', font=('Arial', 10))
#         label_contratacao.grid(row=8, column=0, sticky='w')
#         combo_contratacao = ttk.Combobox(frame_cadastro, values=['Fixa', 'Horista'],width=7, font=('Arial', 10))
#         combo_contratacao.grid(row=8, column=1, sticky='w')

#         label_cargo = tk.Label(frame_cadastro, text='Cargo:', fg='#000000', bg='#FFFFFF', font=('Arial', 10))
#         label_cargo.grid(row=9, column=0, sticky='w')
#         entry_cargo = tk.Entry(frame_cadastro, width=60, font=('Arial', 10), relief='solid')
#         entry_cargo.grid(row=9, column=1, sticky='w')

#         label_salario = tk.Label(frame_cadastro, text='Salário:', fg='#000000', bg='#FFFFFF', font=('Arial', 10))
#         label_salario.grid(row=10, column=0, sticky='w')
#         entry_salario = tk.Entry(frame_cadastro, width=10, font=('Arial', 10), relief='solid')
#         entry_salario.grid(row=10, column=1, sticky='w')

#         label_data_admissao = tk.Label(frame_cadastro, text='Data de admissão:', fg='#000000', bg='#FFFFFF', font=('Arial', 10))
#         label_data_admissao.grid(row=11, column=0, sticky='w')
#         entry_data_admissao = tk.Entry(frame_cadastro, width=40, font=('Arial', 10), relief='solid')
#         entry_data_admissao.grid(row=11, column=1, sticky='w')

#         label_ativo=tk.Label(frame_cadastro, text='Funcionário Ativo:', fg='#000000', bg='#FFFFFF', font=('Arial', 10))
#         label_ativo.grid(row=12, column=0, sticky='w')
#         combo_ativo=ttk.Combobox(frame_cadastro, values=['Sim','Não'],width=5, font=('Arial', 10))
#         combo_ativo.grid(row=12, column=1, sticky='w')

#         botao_salvar = tk.Button(frame_cadastro, text='SALVAR', font=('Arial', 12, 'bold'),
#                                  bg='#00008B', fg='#FFFFFF', width=12, height=1, command=self.salvar_dados)
#         botao_salvar.grid(row=13, column=0,pady=10, sticky="w")

#         botao_novo = tk.Button(frame_cadastro, text='NOVO CADASTRO', font=('Arial', 12, 'bold'),
#                                  bg='#00008B', fg='#FFFFFF',width=15, height=1)
#         botao_novo.grid(row=13, column=1,pady=5, sticky="e")
        
        
#       def salvar_dados(self):
#             confirmar = messagebox.askyesno("Confirmação", "Deseja salvar os dados?")
#             if confirmar:
#                   messagebox.showinfo("Salvo", "Os dados foram salvos com sucesso!")
#             else:
#                   messagebox.showwarning("Cancelado", "O salvamento foi cancelado.")


# if __name__ == "__main__":
#     root = tk.Tk()
#     root.withdraw()
#     app = RegistroFuncionario(master=root)
#     app.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


class RegistroFuncionario(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#FFFFFF")
        self.master = master
        self.pack(fill="both", expand=True)

        self.conectar_banco()
        self.criar_tabela()
        self.dados_funcionario()
        
    def conectar_banco(self):
        self.conn = sqlite3.connect(r'C:\Users\998096\Documents\python\PROJETO_TURMA_RH_SENAC\DATA\database.db')
        self.cursor = self.conn.cursor()

    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                matricula INTEGER UNIQUE NOT NULL,  -- Apenas números
                contato INTEGER,                    -- Apenas números
                idade INTEGER,
                data_nascimento TEXT,               -- Formato de data como string (ex: '2025-06-04')
                cpf INTEGER,                        -- Apenas números
                rg INTEGER,                         -- Apenas números
                tipo_contratacao TEXT CHECK (tipo_contratacao IN ('Fixa', 'Horista')),
                cargo TEXT CHECK (cargo IN ('ADM', 'USER')),  -- ADM ou USER
                salario REAL,
                data_admissao TEXT,                 -- Formato de data como string
                ativo TEXT CHECK (ativo IN ('Sim', 'Não')) DEFAULT 'Sim'
            )
        ''')
        self.conn.commit()


    def dados_funcionario(self):
        # Frame do destaque
        frame_destaque = tk.Frame(self, bg='#00008B')
        frame_destaque.grid(row=0, column=0, sticky='ew')
        self.grid_columnconfigure(0, weight=1)

        label_principal = tk.Label(frame_destaque, text='CADASTRAR FUNCIONÁRIO',
                                   fg="#FFFFFF", bg="#00008B", font=("Arial", 14, "bold"))
        label_principal.pack(anchor='center')

        # Frame principal
        frame_cadastro = tk.Frame(self, bg='#FFFFFF')
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














