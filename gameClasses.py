from txtFileClass import Score
from AUXsFuncs import *
from time import sleep

class Player:
    '''
    responsável por instanciar os jogadores e realizar suas jogadas.
    se comunica com a classe Game.
    '''
    
    def __init__(self, name, score, places):  # MÉTODO CONSTRUTOR
        self.name = name 
        self.score = score
        self.places = places 

    def escolher_lugar(self):
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
    
    board = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]  # TALVEZ O BOARD SEJA FEITO NA MAIN.PY

    def show_blanck_board():
        print("1 | 2 | 3\n- - - - -\n4 | 5 | 6\n- - - - -\n7 | 8 | 9")
    
    def show_board(board):
        board_string = ""
        for enum, place in enumerate(board):
            enum += 1
            if place == 0:
                board_string += "O"
            elif place == 1:
                board_string += "X"
            
            if enum != 3 and enum != 6 and enum != 9:
                board_string += " | "
            if enum == 3 or enum == 6:
                board_string += "\n- - - - -\n"
        print(board_string)


    def set_place():
        pass

    def verify_game_state():
        pass

    def end_game():
        pass


class Menu:
    '''
    realiza a movimentação do jogo, chamando a classe txtFile e fazendo verificações.
    se comunica diretamente com Player, Machine e Game para dar andamento ao jogo
    '''

    def opening():  # inicia o jogo, chamando txtFile para verificar como proceder na abertura
        print("*** JOGO DA VELHA ***")
        sleep(1)
        print("\nInicializando...")
        for c in range(3):
            sleep(1)
            print(".")
        print()
        Refresh()
        print("*** JOGO DA VELHA ***\n")

        if Score.score_verifier() == False:
            print("Parece que é a sua primeira vez aqui...\nVamos jogar?")
            input("\n\nPressione ENTER para continuar... ")
            Refresh()
            return False
        else:
            ScoreData = Score.player_info_getter()
            print("Seus dados foram carregados!\n" +
            f"Jogador 01: { ScoreData[0][0] } | Pontuação: { ScoreData[0][1] }\n" +
            f"Jogador 02: { ScoreData[1][0] } | Pontuação: { ScoreData[1][1] }\n" +
            f"Pontuação da máquina: { ScoreData[2] }")
            input("\n\nPressione ENTER para continuar... ")
            Refresh()
            return ScoreData

    '''def ContinueGame():
        pass'''  # MÉTODO ARQUIVADO / inutilidade

    def new_game():  # simula a iniciação do zero
        print("*** JOGO DA VELHA ***")
        p1_name = Name(1)
        p2_name = Name(2)
        Score.write_data([p1_name, 0], [p2_name, 0], 0)
        input("\nPressione ENTER para continuar... ")
        Refresh()
