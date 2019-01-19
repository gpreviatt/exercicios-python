#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele lendo o nome deles e escrevendo o nome escolhido
from random import randint
aleatorio = randint(0,3)
alunos = ['Pedro', 'Maria', 'Jose', 'Marcos']
print('O aluno que vaia apagar vai ser o {}'.format(alunos[aleatorio]))