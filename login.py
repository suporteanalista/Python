def login():
    username = input("Digite o seu nome de usuário: ")
    password = input("Digite a sua senha: ")

    if username == "admin" and password == "senha123":
        print("Login bem-sucedido!")
    else:
        print("Nome de usuário ou senha incorretos.")

login()