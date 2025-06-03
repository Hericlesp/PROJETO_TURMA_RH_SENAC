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
            self.top_frame, text="GERADOR DE PONTO - ADMIN",
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



        #GERADOR DE CODIGO AQUI
        
        
        
        
        



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
            self.footer_frame, text="GERAR \n PONTO",
            font=("Arial", 14), bg="#0300A7", fg="white",
            width=20, height=2
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

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaPonto(root)
    app.run()
