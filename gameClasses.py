from scoreClass import *
from auxiliaryFuncs import *
from time import sleep

class Player:
    '''
    responsável por instanciar os jogadores e realizar suas jogadas.
    se comunica com a classe Game.
    '''
    
    def __init__(self, name, score):  # MÉTODO CONSTRUTOR
        self.name = name 
        self.score = score
        self.signal = 2

    def choose_place(self, board):  # MÉTODO ONDE O JOGADOR ESCOLHE SEU LUGAR NO TABULEIRO
        '''
        realiza a escolha do local do jogador no tabuleiro.
        se comunica com ... para saber se o local é valido.
        '''
        Refresh()
        finished = Game.verify_game_state(board)
        if finished[0]:
            return board, finished

        placesLeft = Game.places_left(board)
        print(f"*** TURNO DE { self.name } ***\n")
        Game.show_board(board)
        print()
        placeChosen = BoardPlace(placesLeft)
        board = Game.set_place(board, placeChosen, self.signal)
        return board, finished

    def choose_signal(self):  # ESCOLHA VOLUNTÁRIA DO SINAL DO JOGADOR
        self.signal = Menu.choosing_signal(self.name)

    def defined_signal(self, player01):  # ESCOLHA INVOLUNTÁRIA DO SINAL DO JOGADOR
        # MOSTRAR QUE ESSE JOGADOR RECEBEU ESSE SINAL OBRIGATORIAMENTE
        if player01.signal == 1:
            self.signal = 0
        else:
            self.signal = 1


        

class Machine:
    '''
    responsável por atuar como computador/máquina interagindo com o jogador aleatóriamente.
    funciona como a classe Player, mas aleatóriamente.
    é possivel simular uma inteligência artificial...
    '''

    def __init__(self, score):
        self.score = score
    
    def choose_place(self):
        pass



class Game:  # é necessário que os métodos de verificação não alertem no terminal caso a MÁQUINA jogue (adaptar)
    '''
    responsável por controlar o tabuleiro, verificar local e se há vencedor ou empate.
    pode resetar a si próprio.
    '''
    
    # board = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]  # TALVEZ O BOARD SEJA FEITO NA MAIN.PY

    '''def show_blanck_board():
        # printa o tabuleiro em branco com os locais onde o jogador pode escolher jogar
        print("1 | 2 | 3\n- - - - -\n4 | 5 | 6\n- - - - -\n7 | 8 | 9")'''  # MÉTODO ARQUIVADO / substituido
    
    def show_board(board):  # MOSTRA O TABULEIRO
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


    def set_place(board, index, player_signal):  # DEFINE LUGAR NO TABULEIRO
        board[index] = player_signal
        return board

        '''if board[index] == 2:
            board[index] = place
            return True, board
        else:
            return False, board'''  # Pode ser usado como controle ou logger

        '''# [0] > valor / [1] > index
        if board[place_to_put[1]] == 2:
            board[place_to_put[1]] = place_to_put[0]
            return True, board
        else:
            return False, board'''  # ANTIGO USO DO MÉTODO / errado e feio
            

    def verify_game_state(board):  # VERIFICA O STATUS DE VITÓRIA, EMPATE E CONTINUAÇÃO DO JOGO
        # PARA OTIMIZAR, UTILIZAR UM FOR COM O E 1 E VERIFICAR COM METADE DAS LINHAS
        if board[0] == 0 and board[1] == 0 and board[2] == 0:  # VERIFICAÇÃO HORIZONTAL
            return True, 0
        elif board[3] == 0 and board[4] == 0 and board[5] == 0:
            return True, 0
        elif board[6] == 0 and board[7] == 0 and board[8] == 0:
            return True, 0

        elif board[0] == 1 and board[1] == 1 and board[2] == 1:
            return True, 1
        elif board[3] == 1 and board[4] == 1 and board[5] == 1:
            return True, 1
        elif board[6] == 1 and board[7] == 1 and board[8] == 1:
            return True, 1

        elif board[0] == 0 and board[3] == 0 and board[6] == 0:  # VERIFICAÇÃO VERTICAL
            return True, 0
        elif board[1] == 0 and board[4] == 0 and board[7] == 0:
            return True, 0
        elif board[2] == 0 and board[5] == 0 and board[8] == 0:
            return True, 0

        elif board[0] == 1 and board[3] == 1 and board[6] == 1:
            return True, 1
        elif board[1] == 1 and board[4] == 1 and board[7] == 1:
            return True, 1
        elif board[2] == 1 and board[5] == 1 and board[8] == 1:
            return True, 1

        elif board[0] == 0 and board[4] == 0 and board[8] == 0:  # VERIFICAÇÃO DIAGONAL
            return  True, 0
        elif board[2] == 0 and board[4] == 0 and board[6] == 0:
            return  True, 0
        elif board[0] == 1 and board[4] == 1 and board[8] == 1:
            return  True, 1
        elif board[2] == 1 and board[4] == 1 and board[6] == 1:
            return  True, 1

        else:
            if Game.tie_verifier(board):
                return True, 3
            else:
                return False, 2
        

    def game(score, board, multiplayer):  # EXECUTA O JOGO TÉCNICAMENTE
        finished = Game.verify_game_state(board)
        
        if multiplayer:
            player01 = Player(score[0][0], score[0][1])
            player02 = Player(score[1][0], score[1][1])

            player01.choose_signal()
            player02.defined_signal(player01)

            while finished[0] != True:
                board, finished = player01.choose_place(board)
                board, finished = player02.choose_place(board)
                # finish = Game.verify_game_state(board)
            winner = Game.end_game(finished[1], [player01, player02], True)

        else:
            player = Player(score[0][0], score[0][1])
            machine = Player(score[2])

            while finished[0] != True:
                board = player.choose_place(board)
                board = machine.choose_place(board)
                finished = Game.verify_game_state(board)
            winner = Game.end_game(finished[1], [player, machine], False)

        Game.game_conclusion(winner)
        input("\n\nPressione ENTER para continuar...")
        Game.show_board(board)
        return Game.reset_board()


    def places_left(board):  # RETORNA UM ARRAY COM TODOS OS INDEXS DOS LUGARES DISPONIVEIS NO BOARD
        places_left = []
        for num, place in enumerate(board):
            if place == 2:
                places_left.append(num + 1)
            else:
                places_left.append(0)
        return places_left


    def tie_verifier(board):  # VERIFICA EMPATE NO JOGO
        places_left = Game.places_left(board)
        if sum(places_left) == 0:
            return True
        else:
            return False


    def end_game(winnerId, winners, multiplayer):
        # winnerId = 0 or 1 or 2
        # winners = [player, machine] or [player01, player02]
        # multiplayer = True or False
        if multiplayer:
            if winnerId == 2:
                print("*** EMPATE ***")
                print(f"\n\nParece que houve um empate entre vocês dois, { winners[0].name } e { winners[1].name }!\n\n")
                return 2
            else:
                print(f"*** PARABÉNS { winners[0].name if winners[0].signal == winnerId else winners[1].name } ***")
                print("\n\nVocê venceu essa jogada!\n\n")
                return winners[0].name if winners[0].signal == winnerId else winners[1].name
        else:
            if winnerId == 2:
                print("*** EMPATE ***")
                print(f"\n\nParece que você empatou comigo { winners[0].name }!\n\n")
                return 2
            elif winnerId == winners[0].signal:
                print(f"*** VOCÊ VENCEU { winners[0].name } ***")
                print("\n\nVocê conseguiu me superar!\n\n")
                return winners[0].name
            else:
                print(f"*** VOCÊ PERDEU { winners[0].name } ***")
                print("\n\nEu fui mais esperto que você!\n\n")
                return 3


    def game_conclusion(winner):
        player01, player02, machine = Score.player_info_getter()
        if winner == 3:
            Score.write_data(player01, player02, machine + 1)
        else:
            if player01[0] == winner:
                Score.write_data([winner, player01[1] + 1], player02, machine)
            else:
                Score.write_data(player01, [winner, player02[1] + 1], machine)


    def reset_board():  # RESETA O TABULEIRO
        return [ 2, 2, 2,
                 2, 2, 2,
                 2, 2, 2 ]


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


    def choosing_signal(name):  # MÉTODO PARA O JOGADOR ESCOLHER SEU SINAL
        print(f"*** Escolha seu sinal, { name } ***")
        return SignalChoice()


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

    
    def game(score, board):  # Método principal da classe Menu que elabora todo o projeto
        while True:
            print("*** JOGO DA VELHA ***")
            print(f"\nBem vindos { score[0][0] } e { score[1][0] }!\nO que desejam fazer?")
            print(f"\r[ 1 ] Jogar juntos\n\r[ 2 ] Jogar contra máquina\n\r[ 3 ] Ver pontuação\n\r[ 4 ] Configurações\n\r[ 5 ] Sair\n")
            opc = Option("Sua opção >>> ", 5)
            sleep(0.5)
            Refresh()

            if opc == 1:  # MULTIPLAYER
                board = Game.game(score, board, True)

            if opc == 2:  # CONTRA MÁQUINA
                # QUEM JOGA COM A MÁQUINA???
                board = Game.game(score, board, False)

            if opc == 3:  # VER PONTUAÇÃO
                print("*** PONTUAÇÃO ***\n")
                print(f"{ score[0][0] } > { score[0][1] } pontos.\n{ score[1][0] } > { score[1][1] } pontos.\nMáquina > { score[2] } pontos.")
                input("\n\nPressione ENTER para voltar...")

            if opc == 4:  # CONFIG
                print("*** CONFIGURAÇÕES ***")
                print("\nO que deseja fazer?\n\r[ 1 ] Zerar pontuação\n\r[ 2 ] Mudar nomes\n\r[ 3 ] Resetar jogo\n\r[ 4 ] Voltar")
                opc = Option("Sua opção >>> ", 4)
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

                if opc == 4:  # VOLTAR
                    Refresh()

            if opc == 5:  # SAIR
                print("*** FECHANDO ***\n")
                for c in range(3, 0, -1):
                    print(c)
                    sleep(1)
                quit()
        
            Refresh()
