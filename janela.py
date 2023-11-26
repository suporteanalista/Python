# import tkinter

# janela = tkinter.Tk()
# janela.geometry ("500x300")

# def clique():
#     print("Fazer Login")

# texto = tkinter.Label(janela, text="Fazer Login")
# texto.pack(padx=10, pady=10)

# botao = tkinter.Button(janela, text="Login", command=clique)
# botao.pack(padx=10, pady=10)

# janela.mainloop()
import customtkinter

janela = customtkinter.CTk()
janela.geometry ("500x300")

def clique():
    print("Fazer Login")

texto = customtkinter.CTkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text="Seu e-mail")
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Sua senha", show="*")
senha.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="Login", command=clique)
botao.pack(padx=10, pady=10)

janela.mainloop()