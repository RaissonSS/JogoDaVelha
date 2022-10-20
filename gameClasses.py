from txtFileClass import txtFile as Score
from time import sleep
from os import system

class Player:
    pass
    def __init__(self, nome, pontuacao, locaisE):
        self.nome = nome 
        self.pontuacao = pontuacao
        self.locaisE = locaisE 

    #def escolherlugar(self, locau):
        

class Machine:
    pass



class Game:
    
    board = [ [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0] ]

    def SetPlace():
        pass

    def VerifyGameState():
        pass

    def EndGame():
        pass


class Menu:

    def Opening():
        print("*** JOGO DA VELHA ***")
        sleep(1)
        print("Inicializando...")
        for c in range(3):
            sleep(1)
            print(".")
        print()
        refresh()
        verification = Score.ScoreVerifier()
        print(verification)
        print("*** JOGO DA VELHA ***\n\n")

        if verification == False:
            print("Parece que é a sua primeira vez aqui...\nVamos jogar?")
        else:
            print("Seus dados foram carregados!\n" +
            f"Jogador 01: { verification[0][0] } | Pontuação: { verification[0][1] }\n" +
            f"Jogador 02: { verification[1][0] } | Pontuação: { verification[1][1] }\n" +
            f"Máquina: ...")

        input("\n\nPressione ENTER para iniciar... ")
        return verification

    def ContinueGame():
        pass

    def NewGame():
        pass




def refresh():  # limpa o terminal
    system('cls')