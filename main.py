from gameClasses import *

newGame = Menu.Opening()
# OPENING RETORNA TANTO FALSE QUANTO SCORE DATA!!!
if newGame:
    Menu.ContinueGame()
else:
    Menu.NewGame()