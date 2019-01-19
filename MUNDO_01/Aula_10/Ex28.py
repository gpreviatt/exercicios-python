#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador, o computador deverá escrever na tela se o usuário venceu ou perdeu
from random import randint
computador = randint(0, 5)
n = int(input('Em que número eu pensei?: '))
if n == computador:
    print('PARABÉNS você venceu eu pensei no número {} e você digitou {}'.format(computador, n))
else:
    n = int(input('Você PERDEU!\nEu pensei no número {} e você digitou {}'.format(computador,n)))
