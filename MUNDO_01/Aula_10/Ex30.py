#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR
n = int(input('Digite um número'))
if n % 2 == 0:
    print('{} é PAR'.format(n))
else:
    print('{} é IMPAR'.format(n)) 