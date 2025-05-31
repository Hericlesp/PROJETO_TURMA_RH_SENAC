# import tkinter as tk


# class Point(tk.Toplevel):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.title("Cadastro de Funcionário")
#         self.geometry("450x450")
#         self.configure(bg='#FFFFFF')
#         self.criar_interface()

#     def criar_interface(self):
#         center_frame = tk.Frame(self, bg="white")
#         center_frame.pack(fill="both", side="left", expand=True, padx=0, pady=15)

#         nome_lbl = tk.Label(center_frame, text="José Araudo Dos Santos", font=("Arial", 20), bg="white", fg="black")
#         nome_lbl.pack(padx=10)

#         matricula_lbl = tk.Label(center_frame, text="MATRICULA: 85b690", font=("Arial", 10), bg="white", fg="black")
#         matricula_lbl.pack(padx=10)

#         codigo_lbl = tk.Label(center_frame, text="CÓDIGO", font=("Arial", 14, "bold"), bg="white", fg="black")
#         codigo_lbl.pack(padx=10, pady=10)

#         codigo_ety = tk.Entry(center_frame, font=("Arial", 20, "bold"), bg="#f0f0f0", fg="black", width=15, justify="center")
#         codigo_ety.pack(pady=20)

#         # Footer frame
#         self.footer_frame = tk.Frame(center_frame, bg="white")
#         self.footer_frame.pack(fill="both", padx=0, pady=10)

#         self.Regis_Entrada_btn = tk.Button(center_frame, text="Registrar \nEntrada", font=("Arial", 14), bg="#0300A7", fg="white", width=20, height=2)
#         self.Regis_Entrada_btn.pack(pady=10)

# # Programa principal
# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Menu Principal")
#     root.geometry("400x200")

#     tk.Label(root, text="MENU PRINCIPAL", font=("Arial", 16, "bold")).pack(pady=20)

#     tk.Button(root, text="Abrir Cadastro de Funcionário", width=30, height=2,
#               command=lambda: Point(master=root)).pack(pady=10)

#     tk.Button(root, text="Sair", width=30, height=2, command=root.destroy).pack(pady=10)

#     root.mainloop()

    
#     '''
#     gera banco de dado mas  n conecta aos devidos lugares
#     '''
#     # def point():
#     #     DB_DIR = r"C:\Users\998096\Documents\python\PROJETO_TURMA_RH_SENAC\DATA"
#     #     DB_PATH = os.path.join(DB_DIR, 'REGISTER_POINTS.db')

#     #     if not os.path.exists(DB_DIR):
#     #         os.makedirs(DB_DIR)

#     #     conn = sqlite3.connect(DB_PATH)
#     #     cursor = conn.cursor()

#     #     cursor.execute('''CREATE TABLE IF NOT EXISTS Colaborador (
#     #         id INTEGER PRIMARY KEY AUTOINCREMENT,
#     #         RA INT UNIQUE,
#     #         Nome TEXT,
#     #         Setor TEXT,
#     #         Email TEXT,
#     #         Celular INT
#     #     )''')

#     #     cursor.execute('''CREATE TABLE IF NOT EXISTS Entrada (
#     #         id INTEGER PRIMARY KEY AUTOINCREMENT,
#     #         HORA_ENT TEXT,
#     #         STATUS TEXT DEFAULT 'WORKING'
#     #     )''')

#     #     cursor.execute('''CREATE TABLE IF NOT EXISTS Saida (
#     #         id INTEGER PRIMARY KEY AUTOINCREMENT,
#     #         HORA_SAI TEXT,
#     #         STATUS TEXT DEFAULT 'EXIT'
#     #     )''')

#     #     conn.commit()
#     #     conn.close()


import tkinter as tk


def Point(center_frame):
    # Limpa o conteúdo atual do frame central
    for widget in center_frame.winfo_children():
        widget.destroy()

    # ---------- Conteúdo do quadro branco ----------
    nome_lbl = tk.Label(center_frame, text="José Araudo Dos Santos",
                        font=("Arial", 20), bg="white", fg="black")
    nome_lbl.pack(padx=10)

    matricula_lbl = tk.Label(center_frame, text="MATRICULA: 85b690",
                              font=("Arial", 10), bg="white", fg="black")
    matricula_lbl.pack(padx=10)

    codigo_lbl = tk.Label(center_frame, text="CÓDIGO",
                           font=("Arial", 14, "bold"), bg="white", fg="black")
    codigo_lbl.pack(padx=10, pady=10)

    codigo_ety = tk.Entry(center_frame, font=("Arial", 20, "bold"),
                           bg="#f0f0f0", fg="black", width=15, justify="center")
    codigo_ety.pack(pady=20)

    # Footer frame
    footer_frame = tk.Frame(center_frame, bg="white")
    footer_frame.pack(fill="both", padx=0, pady=10)

    Regis_Entrada_btn = tk.Button(center_frame, text="Registrar \nEntrada",
                                  font=("Arial", 14), bg="#0300A7",
                                  fg="white", width=20, height=2)
    Regis_Entrada_btn.pack(pady=10)


if __name__ == "__main__": 
    root = tk.Tk()
    root.title("Cadastro de Funcionário")
    root.geometry("800x400")
    root.configure(bg='#FFFFFF')
    app = Point(root)
    root.mainloop()