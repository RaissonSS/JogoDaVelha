from scoreClass import *
from GameClasses import *
from auxiliaryFuncs import *
from random import randint

placesLeft = [ 1, 2, 3,
               0, 0, 0,
               7, 8, 9 ]
print(Machine.machine_chose_place(placesLeft))