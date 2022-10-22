from os import system


def Name(playerNumber):  # trata inputs destinados ao nome
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


def refresh():  # limpa o terminal
    system('cls')
