from GameClasses import *

newGame = Menu.opening()

if newGame == False:
    gameScore = Menu.new_game()
else:
    gameScore = newGame

board = [ 2, 2, 2,
          2, 2, 2,
          2, 2, 2 ]

Menu.game(gameScore, board)

# PROBLEMA NO verify_game_state