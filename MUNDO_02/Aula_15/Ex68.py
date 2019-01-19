#Faça um programa que jogue PAR ou Impar com o computador. O jogo só será interrompido quando
#o jogador perder mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

from random import randint #importando a biblioteca de números aleatorios inteiros
n = som =0
valor = 0.0
n = int(input('Digite um valor'))
pouimp = (input('Par ou Ímpar? [P/I]'))
while True:
    aleatorio = randint(0, 9)
    valor = n + aleatorio
    if (valor%2) == 0:
        print('Você digitou {} e o computador {} de {} DEU PAR'.format(n,aleatorio,valor))
    if (valor%2) != 0:
        print('Você digitou {} e o computador {} de {} DEU IMPAR'.format(n, aleatorio, valor))

    if pouimp == 'p':
        if (valor%2) == 0:
            print('Você venceu vamos jogar novamente ...')
            som += 1
        if (valor%2) != 0:
            print('VOCE PERDEU!')
            print('Game Over! você venceu {} vezes'.format(som))
            break
    if pouimp == 'i':
        if (valor%2) != 0:
            print('Você venceu vamos jogar novamente ...')
            som +=1
        if (valor%2) == 0:
            print('VOCE PERDEU!')
            print('Game Over! você venceu {} vezes'.format(som))
            break
    n = int(input('Digite um valor'))

