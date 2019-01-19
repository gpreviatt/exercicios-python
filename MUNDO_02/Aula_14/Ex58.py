# melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer.

from random import randint
cont = aleatorio = 0
aleatorio = randint(0,9)
n = int(input('Em que número eu pensei [0 a 9]'))
cont = 0
while n != aleatorio:
    n = int(input('Errado Tente denovo: '))
    cont += 1
print(f'Parabéns, você acerteu e você tentou {cont} vezes')