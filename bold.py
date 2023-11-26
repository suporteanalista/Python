from colorama import init, Fore

# Inicializa o colorama para permitir o uso de cores no console
init()

# Define a mensagem "Fazer Login" em negrito
mensagem = Fore.BOLD + "Fazer Login" + Fore.RESET

# Mostra a mensagem no console
print(mensagem)