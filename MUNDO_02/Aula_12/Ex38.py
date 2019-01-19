#Escreva um programa que leia dois números inteiros e compare -os mostrando na tela uma mensagem -o primeiro é maior, o segundo é maior, não existe valor maior, os dois são iguais
n1 = int(input('Digite um número '))
n2 = int(input('Digite outro número '))

if n1 == n2:
    print('o {} é igual ao {}'.format(n1,n2))
if n1 > n2:
    print('o {} é maior que o {} '.format(n1,n2))
if n2 > n1:
    print('o {} é maior que o {} '.format(n2,n1))