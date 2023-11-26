import tkinter as tk
import customtkinter as CTk
import sqlite3
import hashlib

def create_table():
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT, password TEXT)')
    conn.commit()
    conn.close()

def register_user(username, password):
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    c.execute('INSERT INTO user (username, password) VALUES (?, ?)', (username, hash_password))
    conn.commit()
    conn.close()

def check_login():
    username = entry_username.get()
    password = entry_password.get()
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    c.execute('SELECT * FROM user WHERE username=? AND password=?', (username, hash_password))
    if c.fetchone():
        label_result.config(text="Login bem sucedido!")
    else:
        label_result.config(text="Falha no login. Tente novamente.")
    conn.close()

create_table()
register_user("admin", "password")

root = tk.Tk()
root.title("Interface de Login")

label_username = tk.Label(root, text="Nome de usuário:")
label_username.pack()

entry_username = CTk.CTkEntry(root, bg_color="blue", fg_color="white", font="Arial 12")
entry_username.pack()

label_password = tk.Label(root, text="Senha:")
label_password.pack()

entry_password = CTk.CTkEntry(root, show="*", bg_color="blue", fg_color="white", font="Arial 12")
entry_password.pack()

button_login = CTk.CTkButton(root, text="Login", command=check_login, bg_color="green", fg_color="white", font="Arial 12 bold")
button_login.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()