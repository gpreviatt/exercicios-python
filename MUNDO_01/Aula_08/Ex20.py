#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Fala um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
from random import shuffle
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
alunos = [n1, n2, n3, n4]
shuffle(alunos) #Embaralha a lista
print('A ordem de apresentação será\n{}'.format(alunos))
