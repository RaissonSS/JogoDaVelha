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
        print("\nInicializando...")
        for c in range(3):
            sleep(1)
            print(".")
        print()
        refresh()
        print("*** JOGO DA VELHA ***\n")

        if Score.ScoreVerifier() == False:
            print("Parece que é a sua primeira vez aqui...\nVamos jogar?")
            input("\n\nPressione ENTER para continuar... ")
            refresh()
            return False
        else:
            ScoreData = Score.PlayerInfoGetter()
            print("Seus dados foram carregados!\n" +
            f"Jogador 01: { ScoreData[0][0] } | Pontuação: { ScoreData[0][1] }\n" +
            f"Jogador 02: { ScoreData[1][0] } | Pontuação: { ScoreData[1][1] }\n" +
            f"Pontuação da máquina: { ScoreData[2] }")
            input("\n\nPressione ENTER para continuar... ")
            refresh()
            return ScoreData

    def ContinueGame():
        pass

    def NewGame():
        pass




def refresh():  # limpa o terminal
    system('cls')