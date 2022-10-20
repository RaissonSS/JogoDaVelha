from txtFileClass import txtFile as Score
from TreatedInputs import *
from time import sleep
from os import system

class Player:
    '''
    responsável por instanciar os jogadores e realizar suas jogadas.
    se comunica com a classe Game.
    '''
    
    def __init__(self, name, score, places):  # MÉTODO CONSTRUTOR
        self.name = name 
        self.score = score
        self.places = places 

    def escolherlugar(self):
        '''
        realiza a escolha do local do jogador no tabuleiro.
        se comunica com ... para saber se o local é valido.
        '''
        pass
        

class Machine:
    '''
    responsável por atuar como computador/máquina interagindo com o jogador aleatóriamente.
    funciona como a classe Player, mas aleatóriamente.
    é possivel simular uma inteligência artificial...
    '''
    pass



class Game:  # é necessário que os métodos de verificação não alertem no terminal caso a MÁQUINA jogue (adaptar)
    '''
    responsável por controlar o tabuleiro, verificar local e se há vencedor ou empate.
    pode resetar a si próprio.
    '''
    
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
    '''
    realiza a movimentação do jogo, chamando a classe txtFile e fazendo verificações.
    se comunica diretamente com Player, Machine e Game para dar andamento ao jogo
    '''

    def Opening():  # inicia o jogo, chamando txtFile para verificar como proceder na abertura
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

    '''def ContinueGame():
        pass'''  # MÉTODO ARQUIVADO / inutilidade

    def NewGame():  # simula a iniciação do zero
        print("*** JOGO DA VELHA ***")
        p1_name = Name(1)
        p2_name = Name(2)
        Score.WriteData([p1_name, 0], [p2_name, 0], 0)
        input("\nPressione ENTER para continuar... ")
        refresh()




def refresh():  # limpa o terminal
    system('cls')