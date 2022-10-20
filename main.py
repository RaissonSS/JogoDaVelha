from gameClasses import *

newGame = Menu.Opening()

if newGame:
    Menu.ContinueGame()
else:
    Menu.NewGame()