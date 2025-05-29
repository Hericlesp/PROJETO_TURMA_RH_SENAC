import tkinter as tk
from tkinter import *


class RegistroFuncionario(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cadastro de Funcionário")
        self.geometry("800x400")
        self.configure(bg='#FFFFFF')
        self.dados_funcionario()

    def dados_funcionario(self):
        Label(self, text='CADASTRAR FUNCIONÁRIO',
              fg='#000000', bg='#FFFFFF', font=('Arial', 14)).grid(row=0, column=1, columnspan=5, pady=10)

        Label(self, text='Nome do funcionário:',
              fg='#000000', bg='#FFFFFF').grid(row=1, column=0, sticky=W)
        Entry(self, width=80,
              bg='#FFFFFF', fg='#000000').grid(row=1, column=1, columnspan=5, sticky=W)

        Label(self, text='Idade:',
              fg='#000000', bg='#FFFFFF').grid(row=2, column=3, sticky=W)
        Entry(self, width=10,
              bg='#FFFFFF', fg='#000000').grid(row=2, column=4, sticky=W)

        Label(self, text='Data de nascimento:',
              fg='#000000', bg='#FFFFFF').grid(row=2, column=0, sticky=W)
        Entry(self, width=25,
              bg='#FFFFFF', fg='#000000').grid(row=2, column=1, sticky=W)

        Label(self, text='CPF:',
              fg='#000000', bg='#FFFFFF').grid(row=3, column=0, sticky=W)
        Entry(self, width=25,
              bg='#FFFFFF', fg='#000000').grid(row=3, column=1, sticky=W)

        Label(self, text='RG:',
              fg='#000000', bg='#FFFFFF').grid(row=3, column=3, sticky=W)
        Entry(self, width=25,
              bg='#FFFFFF', fg='#000000').grid(row=3, column=4, sticky=W)

        Label(self, text='Contratação:',
              fg='#000000', bg='#FFFFFF').grid(row=4, column=0, sticky=W)

        Label(self, text='Cargo:',
              fg='#000000', bg='#FFFFFF').grid(row=6, column=0, sticky=W)
        Entry(self, width=40,
              bg='#FFFFFF', fg='#000000').grid(row=6, column=1)

        Label(self, text='Salário (se fixo):',
              fg='#000000', bg='#FFFFFF').grid(row=6, column=3, sticky=E)
        Entry(self, width=10,
              bg='#FFFFFF', fg='#000000').grid(row=6, column=4, sticky=W)

        Label(self, text='Salário (se horista):',
              fg='#000000', bg='#FFFFFF').grid(row=6, column=5, sticky=W)
        Entry(self, width=10,
              bg='#FFFFFF', fg='#000000').grid(row=6, column=6, sticky=E)

        Label(self, text='Data de admissão:',
              fg='#000000', bg='#FFFFFF').grid(row=7, column=0, sticky=W)

        Label(self, text='Data de demissão:',
              fg='#000000', bg='#FFFFFF').grid(row=7, column=3, sticky=W)





''''
ADICIONAR

botao de salvar = que salva os dados dos funcionarios no banco de dados:
sendo:
*tabela funcionarios da empresa
*tabela individual do funcionario

ou tudo lincado po ID

'''
