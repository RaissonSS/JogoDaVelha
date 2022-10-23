from pdb import Restart
import sys
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

    '''def show_blanck_board():
        # printa o tabuleiro em branco com os locais onde o jogador pode escolher jogar
        print("1 | 2 | 3\n- - - - -\n4 | 5 | 6\n- - - - -\n7 | 8 | 9")'''  # MÉTODO ARQUIVADO / substituido
    
    def show_board(board):
        board_string = ""
        for enum, place in enumerate(board):
            enum += 1
            if place == 0:
                board_string += "O"
            elif place == 1:
                board_string += "X"
            else:
                board_string += f"{ enum }"
            
            if enum != 3 and enum != 6 and enum != 9:
                board_string += " | "
            if enum == 3 or enum == 6:
                board_string += "\n- - - - -\n"
        print(board_string)


    def set_place(board):
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

    def opening():  # Inicia o jogo, chamando txtFile para verificar como proceder na abertura
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


    def new_game():  # Simula a iniciação do zero
        print("*** JOGO DA VELHA ***")
        p1_name = Name(1)
        p2_name = Name(2)
        Score.write_data([p1_name, 0], [p2_name, 0], 0)
        input("\nPressione ENTER para continuar... ")
        Refresh()
        return [[p1_name, 0], [p2_name, 0], 0]

    
    def game(score):  # Método principal da classe Menu que elabora todo o projeto
        while True:
            print("*** JOGO DA VELHA ***")
            print(f"\nBem vindos novamente { score[0][0] } e { score[1][0] }!\nO que desejam fazer?")
            print(f"\r[ 1 ] Jogar juntos\n\r[ 2 ] Jogar contra máquina\n\r[ 3 ] Ver pontuação\n\r[ 4 ] Configurações\n\r[ 5 ] Sair\n")
            opc = Option("Sua opção >>> ", 5)
            sleep(0.5)
            Refresh()

            if opc == 1:  # MULTIPLAYER
                pass

            if opc == 2:  # CONTRA MÁQUINA
                pass

            if opc == 3:  # VER PONTUAÇÃO
                print("*** PONTUAÇÃO ***\n")
                print(f"{ score[0][0] } > { score[0][1] } pontos.\n{ score[1][0] } > { score[1][1] } pontos.\nMáquina > { score[2] } pontos.")
                input("\n\nPressione ENTER para voltar...")

            if opc == 4:  # CONFIG
                print("*** CONFIGURAÇÕES ***")
                print("\nO que deseja fazer?\n\r[ 1 ] Zerar pontuação\n\r[ 2 ] Mudar nomes\n\r[ 3 ] Resetar jogo")
                opc = Option("Sua opção >>> ", 3)
                sleep(0.5)
                Refresh()

                if opc == 1:  # RESENTANDO SCORE
                    print("*** RESETANDO PONTUAÇÃO ***\n")
                    for c in range(5):
                        print(".")
                        sleep(0.5)
                    Score.write_data([score[0][0], 0], [score[1][0], 0], 0)
                    score = Score.player_info_getter()
                    print("\nPontuação resetada.")
                    sleep(2)
                    Refresh()

                if opc == 2:  # ALTERANDO NOMES
                    print("*** ALTERAÇÃO DOS NOMES ***\n")
                    score[0][0] = Name(1)
                    score[1][0] = Name(2)
                    Score.write_data([score[0][0], score[0][1]], [score[1][0], score[1][1]], score[2])
                    score = Score.player_info_getter()
                    sleep(2)
                    print("\nNomes alterados com sucesso.")
                    sleep(2)
                    Refresh()

                if opc == 3:  # RESET
                    print("*** RESTAURANDO O JOGO ***")
                    for c in range(5):
                        print(".")
                        sleep(0.5)
                    verification = Score.reset_game()
                    if verification:
                        print("\nJogo restaurado.")
                        print("\nReinicializando em...")
                        for c in range(3, 0, -1):
                            print(c)
                            sleep(1)
                        quit()
                    else:
                        print("\nHouve um erro na tentativa de resetar o jogo...")
                        sleep(2)
                        Refresh()

            if opc == 5:  # SAIR
                print("*** FECHANDO ***\n")
                for c in range(5, 0, -1):
                    print(c)
                    sleep(1)
                quit()
        
            Refresh()

'''Score.write_data(["Raisson", 3], ["Mariane", 5], 7)
score = [["Raisson", 5], ["Mariane", 3], 10]'''
# Menu.game(score)
board = [ 1, 2, 2,
          2, 1, 2,
          2, 2, 1]

print("TABULEIRO")
Game.show_board(board)
