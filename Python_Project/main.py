import tkinter as tk
from tkinter import messagebox
from db_manager import DatabaseManager

class App:
    def __init__(self, root):
        # Instanciar gerenciador de banco de dados
        self.db = DatabaseManager(
            host="localhost",
            user="root",
            password="123321ma",
            database="pythonsql"
        )
        
        # Configurar janela principal
        self.root = root
        self.root.title("Gerenciador de Usuários")
        
        # Configurar interface
        self.setup_ui()

    def setup_ui(self):
        """Configura os elementos da interface gráfica."""
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_name = tk.Entry(frame)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="E-mail:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_email = tk.Entry(frame)
        self.entry_email.grid(row=1, column=1, padx=5, pady=5)

        btn_add = tk.Button(frame, text="Adicionar Usuário", command=self.add_user)
        btn_add.grid(row=2, column=0, columnspan=2, pady=10)

        self.listbox_users = tk.Listbox(self.root, width=50)
        self.listbox_users.pack(pady=10)

        # Inicializar exibição de usuários
        self.display_users()

    def add_user(self):
        """Adiciona um usuário ao banco de dados."""
        name = self.entry_name.get()
        email = self.entry_email.get()

        if not name or not email:
            messagebox.showwarning("Erro", "Por favor, preencha todos os campos!")
            return

        try:
            self.db.insert_user(name, email)
            messagebox.showinfo("Sucesso", "Usuário adicionado com sucesso!")
            self.entry_name.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            self.display_users()
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível adicionar o usuário: {e}")

    def display_users(self):
        """Exibe os usuários cadastrados na lista."""
        users = self.db.fetch_users()
        self.listbox_users.delete(0, tk.END)
        for user in users:
            self.listbox_users.insert(tk.END, f"{user[1]} ({user[2]})")

# Inicializar aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
