import tkinter as tk
from tkinter import *
from tkinter import ttk
import datetime as dt



class SistemaPonto:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de ponto")
        self.root.geometry("450x450")
        self.root.minsize(450, 450)
        self.root.resizable(False, True)
        self.root.configure(bg="white")
        self.root.iconbitmap(r'C:\Users\998096\Documents\python\PROJETO_TURMA_RH_SENAC\pin.png')
        #self.root.iconbitmap(r'C:\Users\Justino\Documents\Hexa\git&github\PROJETO_TURMA_RH_SENAC\pin.png')

        self.criar_widgets()

    def criar_widgets(self):
        # Barra superior
        self.top_frame = tk.Frame(self.root, bg="#F09001", width=900, height=100)
        self.top_frame.pack(fill="x", side="top", padx=0, pady=0)

        self.title_lbl = tk.Label(self.top_frame, text="Ponto Eletrônico", font=("Arial", 20,"bold"), bg="#F09001", fg="black")
        self.title_lbl.pack(padx=10, pady=10)


        #frame do centro
        self.center_frame = tk.Frame(self.root, bg="white", width=900, height=300)
        self.center_frame.pack(fill="both", side="top", padx=0, pady=15)

        self.nome_lbl = tk.Label(self.center_frame, text="José Araudo Dos Santos", font=("Arial", 28), bg="white", fg="black")
        self.nome_lbl.pack(padx=10)


        self.Matricula_lbl = tk.Label(self.center_frame, text=" MATRICULA: 85b690", font=("Arial", 10), bg="white", fg="black")
        self.Matricula_lbl.pack(padx=10)
        
        self.codigo_lbl = tk.Label(self.center_frame, text="CÓDIGO", font=("Arial", 14,"bold"), bg="white", fg="black")
        self.codigo_lbl.pack(padx=10, pady=10)

        codigo_ety = tk.Entry(self.center_frame, font=("Arial", 20, "bold"), bg="#f0f0f0", fg="black", width=15, justify="center") 
        codigo_ety.pack(pady=20)



        #footer frame

        self.footer_frame = tk.Frame(self.root, bg="white", width=900, height=100)
        self.footer_frame.pack(fill="both", padx=0, pady=10)

        Regis_Entrada_btn = tk.Button(self.footer_frame, text="Registrar \n Entrada", font=("Arial", 14), bg="#0300A7", fg="white", width=20, height=2)
        Regis_Entrada_btn.pack(pady=10)


    def run(self):
        self.root.mainloop()

# Programa principal
if __name__ == "__main__":
    root = tk.Tk()
    point = SistemaPonto(root)
    point.run()
