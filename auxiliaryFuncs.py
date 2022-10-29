from os import system

def Name(playerNumber):  # Trata inputs destinados ao nome
    finished = False
    while finished != True:
        name = str(input(f"Digite o nome do { playerNumber }° jogador: ")).strip()
        if name == "":
            print("\nDigite algo!\n")
        elif name.isdigit():
            print("\nDigite um nome válido!\n")
        else:
            finished = True
    print()
    return name.capitalize()


def Option(msg, max, min=1):  # Trata inputs destinados a opções
    finished = False
    while finished != True:
        try:
            x = int(input(msg))
        except:
            print("\nDigite um número!\n")
        else:
            if x > max or x < min:
                print("\nNúmero além do limite!\n")
            else:
                finished = True
    return x


def BoardPlace(placesLeft):  # Retorna o index do lugar escolhido no tabuleiro pelo jogador
    finished = False
    while finished != True:
        try:
            x = int(input("Seu local: "))
        except:
            print("Digite um número!\n")
        else:
            if x not in placesLeft:
                print("Lugar inválido!\n")
            else:
                index = placesLeft.index(x)
                finished = True
    return index

def SignalChoice():  # Faz a escolha do sinal do jogador e retorna o número escolhido
    finished = False
    while finished != True:
        try:
            x = int(input("\r[ 0 ] O\n\r[ 1 ] X\n\nSua escolha >>> "))
        except:
            print("\nDigite um número!\n")
        else:
            if x > 1 or x < 0:
                print("\nDigite uma opção válida!\n")
            else:
                finished = True
    return x


def Refresh():  # Limpa o terminal
    system('cls')
