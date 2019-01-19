#Crie um programa que faça o computador jogar jokenpô com você
from random import randint
from time import sleep
computador = randint(0,2)
itens = ['Pedra', 'Papel', 'Tesoura']
print('''Escolha uma opção
0.PEDRA
1.PAPEL
2.TESOURA
''')
opcao = int(input('Qual é sua jogada '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('O computador escolheu {}\nE Você {}'.format(itens[computador],itens[opcao]))

if computador == 0: # Computador jogou pedra
    if opcao == 0:
        print('EMPATE')
    if opcao == 1:
        print(('VOCE VENCEU'))
    if opcao == 2:
        print('VOCE PERDEU')
if computador == 1: # Computador jogou papel
    if opcao == 0:
        print('VOCE PERDEU!')
    if opcao == 1:
        print(('EMPATE'))
    if opcao == 2:
        print('VOCÊ VENCEU')
if computador == 2: # computador jogou tesoura
    if opcao == 0:
        print('VOCÊ VENCEU')
    if opcao == 1:
        print(('VOCÊ PERDEU'))
    if opcao == 2:
        print('EMPATE')

