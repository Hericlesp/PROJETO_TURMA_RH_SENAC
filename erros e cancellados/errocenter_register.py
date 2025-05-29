import tkinter as tk
from tkinter import *
from tkinter import ttk



class registro_funcionario(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Registro de Funcionário")
        self.geometry("400x300")
        self.create_widgets()

    def registro(self,janela_cadastro): 
        # Lógica para registrar o funcionário
        self.janela_cadastro= janela_cadastro
        self.janela_cadastro.title('cadastro de clientes')
        self.janela_cadastro.geometry('800x400')
        self.janela_cadastro.configure(bg='#FFFFFF')

    def dados_funcionario(self):
        Label(self.janela_cadastro, text='CADASTRAR FUNCIONÁRIO',
              fg='#000000', bg='#FFFFFF', font=('Arial', 14)).grid(row=0, column=1, columnspan=5, pady=10)
        nome=Label(self.janela_cadastro, text='Nome do funcionário:',
              fg='#000000', bg='#FFFFFF').grid(row=1, column=0, sticky=W)
        entrada_nome=Entry(self.janela_cadastro, width=80, 
                           bg='#FFFFFF',fg='#000000', insertbackground='#000000').grid(row=1, column=1,columnspan=5, sticky=W)
        idade=Label(self.janela_cadastro, text='Idade:',
              fg='#000000', bg='#FFFFFF').grid(row=2, column=3, sticky=W)
        entrada_idade=Entry(self.janela_cadastro, width=10, 
                           bg='#FFFFFF',fg='#000000', insertbackground='#000000').grid(row=2, column=4, sticky=W)
        nascimento=Label(self.janela_cadastro, text='Data de nascimento:',
              fg='#000000', bg='#FFFFFF').grid(row=2, column=0, sticky=W)
        entrada_nascimento=Entry(self.janela_cadastro, width=25, 
                           bg='#FFFFFF',fg='#000000', insertbackground='#000000').grid(row=2, column=1, sticky=W)
        cpf=Label(self.janela_cadastro, text='CPF:', 
              fg='#000000', bg='#FFFFFF').grid(row=3, column=0, sticky=W)
        entrada_cpf=Entry(self.janela_cadastro, width=25, 
                           bg='#FFFFFF',fg='#000000', insertbackground='#000000').grid(row=3, column=1, sticky=W)
        rg=Label(self.janela_cadastro, text='RG:', 
              fg='#000000', bg='#FFFFFF').grid(row=3, column=3, sticky=W)
        entrada_rg=Entry(self.janela_cadastro, width=25, 
                           bg='#FFFFFF',fg='#000000', insertbackground='#000000').grid(row=3, column=4, sticky=W)
        
        tipo_contrato=Label(self.janela_cadastro, text='Contratação:',fg='#000000', bg='#FFFFFF').grid(row=4, column=0, sticky=W)

        cargo=Label(self.janela_cadastro, text='Cargo:', 
              fg='#000000', bg='#FFFFFF').grid(row=6, column=0, sticky=W)
        entrada_cargo=Entry(self.janela_cadastro, width=40,
                          bg='#FFFFFF',fg='#000000', insertbackground='#000000').grid(row=6, column=1)
        sal_fixo=Label(self.janela_cadastro, text='Salário (se fixo):', 
              fg='#000000', bg='#FFFFFF').grid(row=6, column=3, sticky=E)
        entrada_salario_f=Entry(self.janela_cadastro, width=10,
                          bg='#FFFFFF',fg='#000000', insertbackground='#000000').grid(row=6, column=4, sticky=W)
        sal_hr=Label(self.janela_cadastro, text='Salário (se horista):', 
              fg='#000000', bg='#FFFFFF').grid(row=6, column=5, sticky=W)
        entrada_cargo=Entry(self.janela_cadastro, width=10,
                          bg='#FFFFFF',fg='#000000', insertbackground='#000000').grid(row=6, column=6,sticky=E)
        admissao=Label(self.janela_cadastro, text='Data de admissão:', 
              fg='#000000', bg='#FFFFFF').grid(row=7, column=0, sticky=W)
        demissao=Label(self.janela_cadastro, text='Data de demissão:', 
              fg='#000000', bg='#FFFFFF').grid(row=7, column=3, sticky=W)                     


        def run(self):
            self.root.mainloop()
        
    
    
if __name__ == "__main__":
    janela_cadastro = tk.Tk()
    app = registro_funcionario(janela_cadastro)
    app.run()