from gameClasses import *

newGame = Menu.opening()

if newGame == False:
    gameScore = Menu.new_game()
else:
    gameScore = newGame

Menu.game(gameScore)

