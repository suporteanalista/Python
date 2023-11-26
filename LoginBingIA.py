import tkinter as tk
import customtkinter as ctk

def check_login():
    username = entry_username.get()
    password = entry_password.get()
    if username == "admin" and password == "password":
        label_result.config(text="Login bem sucedido!")
    else:
        label_result.config(text="Falha no login. Tente novamente.")

root = tk.Tk()
root.title("Interface de Login")

label_username = tk.Label(root, text="Nome de usuário:")
label_username.pack()

entry_username = ctk.CTkEntry(root)
entry_username.pack()

label_password = tk.Label(root, text="Senha:")
label_password.pack()

entry_password = ctk.CTkEntry(root, show="*")
entry_password.pack()

button_login = ctk.CTkButton(root, text="Login", command=check_login)
button_login.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()