import tkinter as tk
import random
import string

# Função para abrir a janela de gerar código
def abrir_gerador_codigo():
    def gerar_codigo():
        codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        codigo_var.set(codigo)

    janela = tk.Toplevel()
    janela.title("Gerar Código de 6 Dígitos")
    janela.geometry("350x200")
    janela.configure(bg='white')
    janela.resizable(False, False)

    tk.Label(janela, text="Código Gerado:", font=("Arial", 14, "bold"), bg="white").pack(pady=10)
    codigo_var = tk.StringVar()
    codigo_entry = tk.Entry(janela, textvariable=codigo_var, font=("Arial", 20, "bold"),
                            bg="#f0f0f0", fg="black", width=10, justify="center")
    codigo_entry.pack(pady=10)

    btn_gerar = tk.Button(janela, text="Gerar Código", font=("Arial", 14), bg="#007ACC", fg="white",
                          command=gerar_codigo, width=15)
    btn_gerar.pack(pady=5)
    





# Exemplo simplificado de menu lateral com o botão adicionado
class SistemaPonto:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Registro de Ponto - ADMIN")
        self.root.geometry("1000x600")
        self.root.minsize(800, 600)
        self.root.configure(bg="white")
        self.criar_widgets()

    def criar_widgets(self):
        self.menu_frame = tk.Frame(self.root, bg="#d9d9d9", width=150)
        self.menu_frame.pack(fill="y", side="left")

        btn_gerar_codigo = tk.Button(
            self.menu_frame, text="🔑 | Gerar Código", bg="#f0f0f0", width=15,
            command=abrir_gerador_codigo
        )
        btn_gerar_codigo.pack(pady=10)

    abrir_gerador_codigo

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaPonto(root)
    root.mainloop()



# limitador de tempo com 29 mimutos, e add um contador ao adm, e ao usuario.