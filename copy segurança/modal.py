import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Janela Principal")
        self.geometry("800x400")
        self.configure(bg="gray")

        # Frame lateral só pra exemplo
        side_frame = tk.Frame(self, bg="#ccc", width=150)
        side_frame.pack(side="left", fill="y")

        btn_abrir = tk.Button(side_frame, text="Abrir Modal", command=self.abrir_modal)
        btn_abrir.pack(pady=20, padx=10)

        # Frame central branco
        self.center_frame = tk.Frame(self, bg="white")
        self.center_frame.pack(side="right", expand=True, fill="both", padx=10, pady=10)

        lbl_central = tk.Label(self.center_frame, text="Conteúdo do Frame Central", bg="white", font=("Arial", 20))
        lbl_central.pack(pady=50)

        self.modal = None  # Guarda referência do frame modal

    def abrir_modal(self):
        if self.modal is not None:
            return  # Modal já aberto

        # Cria frame modal (janela dentro da janela)
        self.modal = tk.Frame(self.center_frame, bg="#eee", bd=2, relief="raised")
        self.modal.place(relx=0.5, rely=0.5, anchor="center", width=400, height=250)

        # Conteúdo da modal
        lbl = tk.Label(self.modal, text="Janela Modal Interna", bg="#eee", font=("Arial", 16))
        lbl.pack(pady=20)

        btn_fechar = tk.Button(self.modal, text="Fechar", command=self.fechar_modal)
        btn_fechar.pack(pady=10)

        # Opcional: bloqueia interação com o centro enquanto modal estiver aberto
        self.center_frame.update()
        self.modal.grab_set()

    def fechar_modal(self):
        if self.modal:
            self.modal.destroy()
            self.modal = None

if __name__ == "__main__":
    app = App()
    app.mainloop()
