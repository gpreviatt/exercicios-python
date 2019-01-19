#Faça um programa que mostre a tabuada de vários números, um de cada vez para cada valor digitado pelo usuário
#O programa será interrompido quando o número digitado for menor que zero

n = mult = 0
while True:
    n = int(input('Digite o número'))
    if n < 0:
        print('Programa Tabuada encerrado VOLTE SEMPRE!')
        break
    for x in range(1,11):
        mult = n*x
        print('{} X {} é: {}'.format(n,x,mult))