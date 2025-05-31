# import tkinter as tk
# from tkinter import *


# class RegistroFuncionario(tk.Toplevel):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.title("Cadastro de Funcionário")
#         self.geometry("800x400")
#         self.configure(bg='#FFFFFF')
#         self.dados_funcionario()

#     def dados_funcionario(self):
#         Label(self, text='CADASTRAR FUNCIONÁRIO',
#               fg='#000000', bg='#FFFFFF', font=('Arial', 14)).grid(row=0, column=1, columnspan=5, pady=10)

#         Label(self, text='Nome do funcionário:',
#               fg='#000000', bg='#FFFFFF').grid(row=1, column=0, sticky=W)
#         Entry(self, width=80,
#               bg='#FFFFFF', fg='#000000').grid(row=1, column=1, columnspan=5, sticky=W)

#         Label(self, text='Idade:',
#               fg='#000000', bg='#FFFFFF').grid(row=2, column=3, sticky=W)
#         Entry(self, width=10,
#               bg='#FFFFFF', fg='#000000').grid(row=2, column=4, sticky=W)

#         Label(self, text='Data de nascimento:',
#               fg='#000000', bg='#FFFFFF').grid(row=2, column=0, sticky=W)
#         Entry(self, width=25,
#               bg='#FFFFFF', fg='#000000').grid(row=2, column=1, sticky=W)

#         Label(self, text='CPF:',
#               fg='#000000', bg='#FFFFFF').grid(row=3, column=0, sticky=W)
#         Entry(self, width=25,
#               bg='#FFFFFF', fg='#000000').grid(row=3, column=1, sticky=W)

#         Label(self, text='RG:',
#               fg='#000000', bg='#FFFFFF').grid(row=3, column=3, sticky=W)
#         Entry(self, width=25,
#               bg='#FFFFFF', fg='#000000').grid(row=3, column=4, sticky=W)

#         Label(self, text='Contratação:',
#               fg='#000000', bg='#FFFFFF').grid(row=4, column=0, sticky=W)

#         Label(self, text='Cargo:',
#               fg='#000000', bg='#FFFFFF').grid(row=6, column=0, sticky=W)
#         Entry(self, width=40,
#               bg='#FFFFFF', fg='#000000').grid(row=6, column=1)

#         Label(self, text='Salário (se fixo):',
#               fg='#000000', bg='#FFFFFF').grid(row=6, column=3, sticky=E)
#         Entry(self, width=10,
#               bg='#FFFFFF', fg='#000000').grid(row=6, column=4, sticky=W)

#         Label(self, text='Salário (se horista):',
#               fg='#000000', bg='#FFFFFF').grid(row=6, column=5, sticky=W)
#         Entry(self, width=10,
#               bg='#FFFFFF', fg='#000000').grid(row=6, column=6, sticky=E)

#         Label(self, text='Data de admissão:',
#               fg='#000000', bg='#FFFFFF').grid(row=7, column=0, sticky=W)

#         Label(self, text='Data de demissão:',
#               fg='#000000', bg='#FFFFFF').grid(row=7, column=3, sticky=W)





# ''''
# ADICIONAR

# botao de salvar = que salva os dados dos funcionarios no banco de dados:
# sendo:
# *tabela funcionarios da empresa
# *tabela individual do funcionario

# ou tudo lincado po ID

# '''



import tkinter as tk


class RegistroFuncionario:
    def __init__(self, master):
        self.master = master
        self.criar_interface()

    def criar_interface(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        titulo = tk.Label(self.master, text='CADASTRAR FUNCIONÁRIO',
                          fg='#000000', bg='#FFFFFF', font=('Arial', 18, 'bold'))
        titulo.grid(row=0, column=0, columnspan=6, pady=10)

        tk.Label(self.master, text='Nome do funcionário:', bg='#FFFFFF').grid(row=1, column=0, sticky='w')
        tk.Entry(self.master, width=50, bg='#FFFFFF').grid(row=1, column=1, columnspan=3, sticky='w')

        tk.Label(self.master, text='Idade:', bg='#FFFFFF').grid(row=2, column=3, sticky='w')
        tk.Entry(self.master, width=10, bg='#FFFFFF').grid(row=2, column=4, sticky='w')

        tk.Label(self.master, text='Data de nascimento:', bg='#FFFFFF').grid(row=2, column=0, sticky='w')
        tk.Entry(self.master, width=20, bg='#FFFFFF').grid(row=2, column=1, sticky='w')

        tk.Label(self.master, text='CPF:', bg='#FFFFFF').grid(row=3, column=0, sticky='w')
        tk.Entry(self.master, width=20, bg='#FFFFFF').grid(row=3, column=1, sticky='w')

        tk.Label(self.master, text='RG:', bg='#FFFFFF').grid(row=3, column=3, sticky='w')
        tk.Entry(self.master, width=20, bg='#FFFFFF').grid(row=3, column=4, sticky='w')

        tk.Label(self.master, text='Cargo:', bg='#FFFFFF').grid(row=4, column=0, sticky='w')
        tk.Entry(self.master, width=40, bg='#FFFFFF').grid(row=4, column=1, sticky='w')

        tk.Label(self.master, text='Salário (fixo):', bg='#FFFFFF').grid(row=4, column=3, sticky='w')
        tk.Entry(self.master, width=10, bg='#FFFFFF').grid(row=4, column=4, sticky='w')

        tk.Label(self.master, text='Salário (horista):', bg='#FFFFFF').grid(row=4, column=5, sticky='w')
        tk.Entry(self.master, width=10, bg='#FFFFFF').grid(row=4, column=6, sticky='w')

        tk.Label(self.master, text='Data de admissão:', bg='#FFFFFF').grid(row=5, column=0, sticky='w')
        tk.Entry(self.master, width=20, bg='#FFFFFF').grid(row=5, column=1, sticky='w')

        tk.Label(self.master, text='Data de demissão:', bg='#FFFFFF').grid(row=5, column=3, sticky='w')
        tk.Entry(self.master, width=20, bg='#FFFFFF').grid(row=5, column=4, sticky='w')

        # Botão salvar (para implementar função de banco depois)
        salvar_btn = tk.Button(self.master, text='Salvar Funcionário',
                               bg='#007ACC', fg='white', width=20, height=2)
        salvar_btn.grid(row=6, column=0, columnspan=2, pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Cadastro de Funcionário")
    root.geometry("800x400")
    root.configure(bg='#FFFFFF')

    app = RegistroFuncionario(root)
    root.mainloop()