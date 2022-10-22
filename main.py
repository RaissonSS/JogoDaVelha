from gameClasses import *

newGame = Menu.Opening()
# OPENING RETORNA TANTO FALSE QUANTO SCORE DATA!!!
if newGame == False:
    Menu.NewGame()
else:
    Menu.ContinueGame()