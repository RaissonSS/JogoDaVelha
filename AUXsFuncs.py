from os import system

def Name(playerNumber):  # Trata inputs destinados ao nome                          # está funcionando
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


def Option(msg, max, min=1):  # Trata inputs destinados a opções         # está funcionando
    finished = False
    while finished != True:
        try:
            x = int(input(msg))
        except:
            print("\nDigite um número!\n")
        else:
            if x > max or x < min:
                print("\nNúmero além do limite!\n")        # não seri numero invalido para este jogo
            else:
                finished = True
    return x
            

def Refresh():  # Limpa o terminal                      # está funcionando
    system('cls')
