from scoreClass import *
from GameClasses import *
from auxiliaryFuncs import *

'''
não tem necessidade de copiar e colar todas as classes aqui.
eu já estou importando todas elas nos imports aqui em cima, então é só chamar o que tu quer testar

e viu, o teu ultimo commit marcava que tu deu um merge entre duas branches, entao toma muito cuidado
pq tu pode desfazer alguma coisa, nao sei o que tu fez pra dar aquilo

nunca esquece do git pull SEMPRE antes de codar.
se der algum erro, exclui tudo e da o git clone na nova pasta vazia.

quero que tu teste todos os métodos, principalmente de GameClasses, porque são os mais críticos e importantes
de toda essa aplicação, ScoreClasse e AUXsFuncs já foram testados por mim.

(pode copiar tudo de main.py e testar aqui)

se algum exception aparecer em um teste teu, analisa caso não foi um teste mal feito da tua parte,
já que o jogo exige uma 'continuidade' e tu está forçando ela pra testar (já me aconteceu).

se achar um exception e conseguir resolver, não apaga o que tu acha que estava errado, só comenta e deixa a tua parte corrigida
e da o commit (não esquece de testar em cima daquilo que tu corrigiu).

se tu tentou de tudo e não conseguiu, documenta bem o erro que tu atingiu pra eu analisar depois.

se não der nenhum erro, significa que a principio está correto, mas nem sempre, não tem necessidade de 
por um '# funcionando'.

nunca da um commit com mais de uma correção ou teste, sempre individualiza tudo o que tu fizer pra diminuir
a probabilidade de corrupção/confusão/irredutibilidade do código

bons testes QA, besos ;)
'''

board = [ 1, 1, 1,
          1, 1, 1,
          1, 1, 1 ]

print(Game.places_left(board))
print(f"1 - {board} - {type(board)}")