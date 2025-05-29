#informaçoes de contato dos programadores

import tkinter as tk
from tkinter import *


class help:
    def infohelp():
        root = tk.Tk()
        root.title("Ajuda")
        root.geometry("400x300")
        root.configure(bg="#F0F0F0")

        Label(root, text="Informações de Contato", font=("Arial", 16, "bold"), bg="#F0F0F0").pack(pady=10)

        Label(root, text="Desenvolvedores:", font=("Arial", 14), bg="#F0F0F0").pack(pady=5)
        Label(root, text="Justino Araújo", bg="#F0F0F0").pack()
        Label(root, text="José Araújo", bg="#F0F0F0").pack()

        Button(root, text="Fechar", command=root.destroy).pack(pady=20)
