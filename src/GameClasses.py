from src.ScoreClass import *
from auxiliary.AuxiliaryFuncs import *
from time import sleep
from random import randint

class Player:
    '''
    Responsável por representar os jogadores e realizar suas ações, sejam elas jogar ou determinar o sinal.
    '''
    
    def __init__(self, name, score):  # MÉTODO CONSTRUTOR
        self.name = name
        self.score = score
        self.machine = False
        self.signal = 2  # sinal padrão (não escolhido)

    def choose_place(self, board):  # MÉTODO ONDE O JOGADOR ESCOLHE SEU LUGAR NO TABULEIRO
        Refresh()
        finished = Game.verify_game_state(board)
        # Verifica se o jogo já foi vencido antes do próximo jogador jogar
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

    def defined_signal(self, player):  # ESCOLHA INVOLUNTÁRIA DO SINAL DO JOGADOR
        if player.signal == 1:
            self.signal = 0
        else:  # Verifica o sinal do primeiro jogador e determina o sinal do segundo
            self.signal = 1


class Machine:
    '''
    Responsável por atuar como computador/máquina interagindo com o jogador aleatóriamente.
    Funciona como a classe Player, mas aleatóriamente e sem visualização ou interação com o usuário.
    '''

    def __init__(self, score):  # MÉTODO CONSTRUTOR
        self.score = score
        self.machine = True
        self.signal = 2
    
    def choose_place(self, board):  # MÉTODO ONDE A MÁQUINA ESCOLHE SEU LUGAR ALEATORIAMENTE
        finished = Game.verify_game_state(board)
        if finished[0]:
            Refresh()
            return board, finished

        placesLeft = Game.places_left(board)
        while True:
            # A máquina escolhe um lugar, que é verificado, até ser possível
            place = randint(1, 9)
            if place in placesLeft:
                board = Game.set_place(board, placesLeft.index(place), self.signal)
                Machine.machine_playing()
                return board, finished
    
    '''def intelligence_place(self, board):
        pass'''  # Método arquivado
        
    def machine_playing():  # AVISA O JOGADOR QUE A MÁQUINA ESTÁ JOGANDO
        Refresh()
        print("*** MEU TURNO ***")
        print("\n\nEstou pensando...\n\n")
        sleep(0.5)
        print("Joguei!")
        sleep(0.5)
        Refresh()

    def choose_signal(self, player):  # DETERMINA INVOLUNTARIAMENTE O SINAL DA MÁQUINA
        self.signal = 1 if player.signal == 0 else 0


class Game:
    '''
    Responsável por controlar e gerir todo o funcionamento do jogo, como verificar e realizar as jogadas,
    assim como verificar se houveram vitórias ou empates.
    '''
    
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
                # Se o index do número ou sinal no array do tabuleiro NÃO for a "borda" do mesmo, separa os números ou sinais.
                board_string += " | "
            if enum == 3 or enum == 6:
                # Se o index do número ou sinal no array do tabuleiro FOR a primeira ou segunda "borda" do mesmo, divide horizontalmente
                board_string += "\n- - - - -\n"
        print(board_string)

    def set_place(board, index, player_signal):  # DEFINE LUGAR NO TABULEIRO
        board[index] = player_signal
        return board   

    def verify_game_state(board):  # VERIFICA O STATUS DE VITÓRIA, EMPATE E CONTINUAÇÃO DO JOGO
        for num in range(0, 2):
            if board[0] == num and board[1] == num and board[2] == num:  # VERIFICAÇÃO HORIZONTAL
                return True, num
            elif board[3] == num and board[4] == num and board[5] == num:
                return True, num
            elif board[6] == num and board[7] == num and board[8] == num:
                return True, num

            elif board[0] == num and board[3] == num and board[6] == num:  # VERIFICAÇÃO VERTICAL
                return True, num
            elif board[1] == num and board[4] == num and board[7] == num:
                return True, num
            elif board[2] == num and board[5] == num and board[8] == num:
                return True, num

            elif board[0] == num and board[4] == num and board[8] == num:  # VERIFICAÇÃO DIAGONAL
                return  True, num
            elif board[2] == num and board[4] == num and board[6] == num:
                return  True, num

        else:  # Se não houve nenhuma vitória...
            if Game.tie_verifier(board):  # Se houve um empate...
                return True, 3
            else:
                return False, 2  # Não houve nada, então o tabuleiro não está completo para um final ocorrer...

    def game(score, board, multiplayer):  # EXECUTA O JOGO TÉCNICAMENTE
        finished = Game.verify_game_state(board)
        
        if multiplayer:
            player01 = Player(score[0][0], score[0][1])
            player02 = Player(score[1][0], score[1][1])

            player01.choose_signal()
            player02.defined_signal(player01)

            Refresh()
            Menu.show_signals(player01, player02)

            while finished[0] != True:
                board, finished = player01.choose_place(board)
                board, finished = player02.choose_place(board)
            winner = Game.end_game(finished[1], [player01, player02], True, board)

        else:
            player = AgainstMachine(score)
            player = Player(player[0], player[1])
            machine = Machine(score[2])

            player.choose_signal()
            machine.choose_signal(player)

            Refresh()
            Menu.show_signals(player, machine)

            while finished[0] != True:
                board, finished = player.choose_place(board)
                board, finished = machine.choose_place(board)
                finished = Game.verify_game_state(board)
            winner = Game.end_game(finished[1], [player, machine], False, board)

        Game.game_conclusion(winner)
        input("\n\nPressione ENTER para continuar...")
        Game.show_board(board)
        return Game.reset_board()

    def places_left(board):  # RETORNA UM ARRAY COM TODOS OS INDEXS DOS LUGARES DISPONIVEIS NO BOARD
        places_left = []
        for num, place in enumerate(board):
            if place == 2:  # Se a informação naquele local for um 2, ninguém jogou nada ali, então aquele index está disponível para ser escolhido.
                places_left.append(num + 1)
            else:  # Se a informação naquele local não for um 2, aquele local já foi ocupado, portanto, será zero.
                places_left.append(0)
                # Um zero jamais poderia ser escolhido, mas esse index não poderia ser omitido, então permanece zero.
        return places_left

    def tie_verifier(board):  # VERIFICA EMPATE NO JOGO
        places_left = Game.places_left(board)
        if sum(places_left) == 0:
            # Se a soma de todos os números (indexs) for zero, significa que todos foram ocupados.
            return True
        else:
            return False

    def end_game(winnerId, winners, multiplayer, board):  # MOSTRA MENSAGEM DE FINALIZAÇÃO DO JOGO
        # winnerId = 0 or 1 or 3
        # winners = [player, machine] or [player01, player02]
        # multiplayer = True or False
        if multiplayer:
            if winnerId == 3:
                print("*** EMPATE ***\n")
                Game.show_board(board)
                print(f"\n\nParece que houve um empate entre vocês dois, { winners[0].name } e { winners[1].name }!")
                return 2
            else:
                print(f"*** PARABÉNS { winners[0].name if winners[0].signal == winnerId else winners[1].name } ***\n")
                Game.show_board(board)
                print("\n\nVocê venceu essa jogada!")
                return winners[0].name if winners[0].signal == winnerId else winners[1].name
        else:
            if winnerId == 3:
                print("*** EMPATE ***\n")
                Game.show_board(board)
                print(f"\n\nParece que você empatou comigo { winners[0].name }!")
                return 2
            elif winnerId == winners[0].signal:
                print(f"*** VOCÊ VENCEU { winners[0].name } ***\n")
                Game.show_board(board)
                print("\n\nVocê conseguiu me superar!")
                return winners[0].name
            else:
                print(f"*** VOCÊ PERDEU { winners[0].name } ***\n")
                Game.show_board(board)
                print("\n\nEu fui mais esperto que você!")
                return 3

    def game_conclusion(winner):  # CADASTRA DADOS DO VENCEDOR E ATUALIZA PONTUAÇÃO
        player01, player02, machine = Score.player_info_getter()
        if winner == 3:
            Score.write_data(player01, player02, machine + 1)
        else:
            if player01[0] == winner:
                Score.write_data([player01[0], player01[1] + 1], player02, machine)
            elif player02[0] == winner:
                Score.write_data(player01, [player02[0], player02[1] + 1], machine)
            else:
                pass  # EMPATE (nenhuma pontuação é salva)

    def reset_board():  # RESETA O TABULEIRO
        return [ 2, 2, 2,
                 2, 2, 2,
                 2, 2, 2 ]


class Menu:
    '''
    Realiza a movimentação do jogo, chamando a classe txtFile e fazendo verificações.
    Se comunica diretamente com Player, Machine e Game para dar andamento ao jogo.
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

    def show_signals(player01, player02):  # MOSTRA OS SINAIS DOS JOGADORES
        print("*** SINAIS ESCOLHIDOS ***\n")
        print(f"{ player01.name } é { 'X' if player01.signal == 1 else 'O'  }")
        print(f"{ 'Máquina' if player02.machine else player02.name } é { 'X' if player02.signal == 1 else 'O' }")
        input("\n\nPressione ENTER para continuar...")
        Refresh()

    def new_game():  # INICIA O JOGO DO ZERO
        print("*** JOGO DA VELHA ***\n")
        p1_name = Name(1)
        p2_name = Name(2)
        Score.write_data([p1_name, 0], [p2_name, 0], 0)
        input("\nPressione ENTER para continuar... ")
        Refresh()
        return [[p1_name, 0], [p2_name, 0], 0]

    def game(score, board):  # MÉTODO MENU (COORDENA TODO O JOGO)
        while True:
            print("*** JOGO DA VELHA ***")
            print(f"\nBem vindos { score[0][0] } e { score[1][0] }!\nO que desejam fazer?")
            print(f"\r[ 1 ] Jogar juntos\n\r[ 2 ] Jogar contra máquina\n\r[ 3 ] Ver pontuação\n\r[ 4 ] Configurações\n\r[ 5 ] Informações\n\r[ 6 ] Sair\n")
            opc = Option("Sua opção >>> ", 6)
            sleep(0.5)
            Refresh()

            if opc == 1:  # MULTIPLAYER
                board = Game.game(score, board, True)

            if opc == 2:  # CONTRA MÁQUINA
                board = Game.game(score, board, False)

            if opc == 3:  # VER PONTUAÇÃO
                score = Score.player_info_getter()
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

            if opc == 5:  # INFORMAÇÕES
                print("*** INFORMAÇÕES ***")
                print("\nJogo da Velha - Versão 1.5\nDesenvolvedor: Raisson Souza\nTester: Mariane Pigato")
                print("\nVersão 1.0\n\r- Jogo completo")
                print("\nVersão 2.0\n\r- Inteligência Artificial\n\r- Salvamento do último acesso\n\r- Salvamento do número de empates")
                print("\nGitHub: github.com/RaissonSS")
                input("\n\nPressione ENTER para voltar...")

            if opc == 6:  # SAIR
                print("*** FECHANDO ***\n")
                for c in range(3, 0, -1):
                    print(c)
                    sleep(1)
                quit()
        
            Refresh()
