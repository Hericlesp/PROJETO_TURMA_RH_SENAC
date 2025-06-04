# import tkinter as tk
# import random
# import string


# # 🎯 Função para abrir a janela de gerar código
# def abrir_gerador_codigo():
#     def gerar_codigo():
#         codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
#         codigo_var.set(codigo)
#         iniciar_contagem()
#         btn_gerar.config(state="disabled")  # 🔒 Desativa o botão após gerar

#     def iniciar_contagem():
#         nonlocal tempo_restante
#         tempo_restante = 29 * 60  # 29 minutos em segundos
#         atualizar_contagem()

#     def atualizar_contagem():
#         if tempo_restante >= 0:
#             minutos = tempo_restante // 60
#             segundos = tempo_restante % 60
#             tempo_formatado = f"{minutos:02d}:{segundos:02d}"
#             contador_var.set(tempo_formatado)
#             janela.after(1000, decrementar_contagem)
#         else:
#             contador_var.set("Expirado")
#             codigo_var.set("------")
#             btn_gerar.config(state="normal")  # 🔓 Ativa novamente quando expirar

#     def decrementar_contagem():
#         nonlocal tempo_restante
#         tempo_restante -= 1
#         atualizar_contagem()

#     # 🔲 Cria a janela Toplevel
#     janela = tk.Toplevel()
#     janela.title("Gerar Código de 6 Dígitos")
#     janela.geometry("400x250")
#     janela.configure(bg='white')
#     janela.resizable(False, False)

#     tempo_restante = -1

#     # Label título
#     tk.Label(
#         janela, text="Código Gerado:", font=("Arial", 14, "bold"), bg="white"
#     ).pack(pady=10)

#     # Campo onde aparece o código
#     codigo_var = tk.StringVar()
#     codigo_entry = tk.Entry(
#         janela, textvariable=codigo_var, font=("Arial", 20, "bold"),
#         bg="#f0f0f0", fg="black", width=10, justify="center"
#     )
#     codigo_entry.pack(pady=10)

#     # 🕐 Label do contador
#     contador_var = tk.StringVar(value="00:00")
#     contador_lbl = tk.Label(
#         janela, textvariable=contador_var, font=("Arial", 16, "bold"),
#         fg="red", bg="white"
#     )
#     contador_lbl.pack(pady=5)

#     # 🔘 Botão de gerar
#     btn_gerar = tk.Button(
#         janela, text="🔄 Gerar Código", font=("Arial", 14),
#         bg="#007ACC", fg="white", width=15,
#         command=gerar_codigo
#     )
#     btn_gerar.pack(pady=5)


# # 🔧 Classe do sistema principal (com botão do gerador)
# class SistemaPonto:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Sistema de Registro de Ponto - ADMIN")
#         self.root.geometry("1000x600")
#         self.root.minsize(800, 600)
#         self.root.configure(bg="white")
#         self.criar_widgets()

#     def criar_widgets(self):
#         # Menu lateral
#         self.menu_frame = tk.Frame(self.root, bg="#d9d9d9", width=150)
#         self.menu_frame.pack(fill="y", side="left")

#         # Botão: Gerar Código
#         btn_gerar_codigo = tk.Button(
#             self.menu_frame, text="🔑 | Gerar Código", bg="#f0f0f0", width=15,
#             command=abrir_gerador_codigo
#         )
#         btn_gerar_codigo.pack(pady=10)


# # 🚀 Executando
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = SistemaPonto(root)
#     root.mainloop()


import tkinter as tk
from tkinter import messagebox
import sqlite3
import subprocess

def fazer_login():
    ra = entry_usuario.get()
    senha = entry_senha.get()

    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    cursor.execute("SELECT tipo FROM usuarios WHERE ra = ? AND senha = ?", (ra, senha))
    resultado = cursor.fetchone()

    conn.close()

    if resultado:
        tipo = resultado[0]
        messagebox.showinfo("Login", f"Bem-vindo, {tipo.upper()}!")

        if tipo == "root":
            janela.destroy()
            subprocess.Popen(['python', 'root_interface.py'])
        elif tipo == "admin":
            janela.destroy()
            subprocess.Popen(['python', 'admin_interface.py'])
        elif tipo == "usuario":
            janela.destroy()
            subprocess.Popen(['python', 'user_interface.py'])
        else:
            messagebox.showerror("Erro", "Permissão desconhecida!")
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

# Interface Tkinter
janela = tk.Tk()
janela.title("Login")
janela.geometry("300x200")
janela.resizable(False, False)

tk.Label(janela, text="RA (Usuário)").pack(pady=5)
entry_usuario = tk.Entry(janela)
entry_usuario.pack()

tk.Label(janela, text="Senha").pack(pady=5)
entry_senha = tk.Entry(janela, show="*")
entry_senha.pack()

tk.Button(janela, text="Entrar", command=fazer_login).pack(pady=20)

janela.mainloop()
