#Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor a ser sacado (inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues
#Considere que o caixa possui cédulas de R$50 R$50 R$20 R$10 R$5 e R$1
valor = int(input('Qual o valor você quer sacar? R$: '))
total = valor
ced = 100 #valor da maior cedula disponível
totalced = 0 #total de cedulas
while True:
    #Decrementando o valor digitado e guardando a quantidade de cédulas necessárias
    if total >= ced:
        total -= ced
        totalced +=1
    #verifica quantas cédulas daquele valor precisam e imprime até chegar a 0
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totalced = 0
        if total == 0:
            break
