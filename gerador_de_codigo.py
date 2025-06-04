import tkinter as tk
from tkinter import ttk
import sqlite3
import os
import random
import string
from datetime import datetime
import DATABASE


DB_DIR = r"C:\Users\998096\Documents\python\PROJETO_TURMA_RH_SENAC\DATA"
DB_PATH = os.path.join(DB_DIR, 'REGISTER_POINTS.db')


class TelaGerarCodigo:
    def __init__(self, master):
        self.janela = tk.Toplevel(master)
        self.janela.title("Gerar Código - ADMIN")
        self.janela.geometry("600x500")
        self.janela.configure(bg="white")
        self.janela.resizable(False, False)

        self.nome_var = tk.StringVar()
        self.ra_var = tk.StringVar()
        self.codigo_var = tk.StringVar(value="------")
        self.contador_var = tk.StringVar(value="00:00")
        self.tipo_var = tk.StringVar(value="Entrada")

        self.tempo_restante = 0
        self.funcionario_id = None
        self.contagem_ativa = False

        self.criar_widgets()
        self.carregar_admin()

    def criar_widgets(self):
        self.top_frame = tk.Frame(self.janela, bg="#F09001", height=70)
        self.top_frame.pack(fill="x")

        tk.Label(
            self.top_frame, text="GERADOR DE PONTO - ADMIN",
            font=("Arial", 18, "bold"), bg="#F09001", fg="black"
        ).pack(pady=15)

        self.center_frame = tk.Frame(self.janela, bg="white")
        self.center_frame.pack(pady=10)

        tk.Label(self.center_frame, textvariable=self.nome_var,
                 font=("Arial", 20, "bold"), bg="white").pack(pady=5)

        tk.Label(self.center_frame, textvariable=self.ra_var,
                 font=("Arial", 14), bg="white").pack(pady=5)

        tk.Label(self.center_frame, text="CÓDIGO ATUAL:",
                 font=("Arial", 14, "bold"), bg="white").pack(pady=5)

        tk.Entry(self.center_frame, textvariable=self.codigo_var,
                 font=("Arial", 20, "bold"), width=10, justify="center",
                 state="readonly", bg="#f0f0f0").pack(pady=5)

        tk.Label(self.center_frame, textvariable=self.contador_var,
                 font=("Arial", 16, "bold"), fg="red", bg="white").pack(pady=5)

        self.gerar_btn = tk.Button(
            self.center_frame, text="🔑 | GERAR CÓDIGO", width=20,
            font=("Arial", 14), bg="#007ACC", fg="white",
            command=self.gerar_codigo
        )
        self.gerar_btn.pack(pady=10)

        tk.Label(self.center_frame, text="Tipo de Registro:",
                 font=("Arial", 14), bg="white").pack(pady=5)

        self.tipo_cbx = ttk.Combobox(
            self.center_frame,
            values=["Entrada", "Almoço", "Retorno", "Saída"],
            font=("Arial", 12), state="readonly",
            textvariable=self.tipo_var
        )
        self.tipo_cbx.pack(pady=5)
        self.tipo_cbx.set("Entrada")

        self.footer_frame = tk.Frame(self.janela, bg="white")
        self.footer_frame.pack(pady=15)

        tk.Button(
            self.footer_frame, text="FECHAR", width=20,
            font=("Arial", 12), bg="red", fg="white",
            command=self.janela.destroy
        ).pack()

    def gerar_codigo(self):
        if self.contagem_ativa:
            return  # Já está contando, não permite gerar outro

        codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        self.codigo_var.set(codigo)
        self.salvar_codigo(codigo)

        self.tempo_restante = 30 * 60  # 30 minutos
        self.contagem_ativa = True
        self.gerar_btn.config(state="disabled")
        self.atualizar_contagem()

    def atualizar_contagem(self):
        minutos = self.tempo_restante // 60
        segundos = self.tempo_restante % 60
        self.contador_var.set(f"{minutos:02d}:{segundos:02d}")

        if self.tempo_restante > 0:
            self.tempo_restante -= 1
            self.janela.after(1000, self.atualizar_contagem)
        else:
            self.contagem_ativa = False
            self.contador_var.set("Expirado")
            self.codigo_var.set("------")
            self.salvar_codigo("")
            self.gerar_btn.config(state="normal")

    def salvar_codigo(self, codigo):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Atualiza o código no colaborador
        cursor.execute(
            "UPDATE Colaborador SET Codigo = ? WHERE RA = ?",
            (codigo, 998096)
        )

        # Grava no histórico de códigos gerados
        if codigo != "":  # Só salva se for um código gerado, não quando limpa
            data_atual = datetime.now().strftime("%Y-%m-%d")
            hora_atual = datetime.now().strftime("%H:%M:%S")
            tipo = self.tipo_var.get()

            cursor.execute('''
                INSERT INTO Registros_Codigos (colaborador_id, data, hora, codigo, tipo)
                VALUES (?, ?, ?, ?, ?)
            ''', (self.funcionario_id, data_atual, hora_atual, codigo, tipo))

        conn.commit()
        conn.close()

    def carregar_admin(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT id, Nome, RA FROM Colaborador WHERE RA = ?", (998096,))
        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            self.funcionario_id = resultado[0]
            self.nome_var.set(resultado[1])
            self.ra_var.set(f"MATRICULA: {resultado[2]}")
        else:
            self.nome_var.set("ADMIN NÃO ENCONTRADO")
            self.ra_var.set("")
            
    def manter_no_topo(self):
        self.janela.attributes("-topmost", True)

    def liberar_topo(self):
        self.janela.attributes("-topmost", False)


# 🏠 Teste simples com Menu Principal
if __name__ == "__main__":
    from DATABASE import criar_banco_e_tabelas  # Usa o arquivo do banco externo
    criar_banco_e_tabelas()

    root = tk.Tk()
    root.title("Menu Principal")
    root.geometry("400x300")
    root.configure(bg="white")

    tk.Label(root, text="MENU PRINCIPAL", font=("Arial", 18, "bold"), bg="white").pack(pady=20)

    tk.Button(
        root, text="Abrir Gerador de Código", width=25, height=2,
        bg="#007ACC", fg="white", font=("Arial", 12, "bold"),
        command=lambda: TelaGerarCodigo(root)
    ).pack(pady=10)

    tk.Button(
        root, text="Sair", width=25, height=2,
        bg="red", fg="white", font=("Arial", 12, "bold"),
        command=root.quit
    ).pack(pady=10)

    root.mainloop()
