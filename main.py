from GameClasses import *

newGame = Menu.opening()  # Faz a abertura e verificação do arquivo score.txt

if newGame == False:
    gameScore = Menu.new_game()  # Inicia do zero caso o arquivo não exista
else:
    gameScore = newGame  # Salva os dados de pontuação na variável

board = [ 2, 2, 2,
          2, 2, 2,
          2, 2, 2 ]  # Tabuleiro vazio

Menu.game(gameScore, board)  # Chama o método mestre que coordena todo o jogo
