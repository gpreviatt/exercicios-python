#Crie um programa que leia dois valores e motre um menu na tela
#[1] Somar
#{2} Multiplicar
#[3] Maior
#[4] Novos números
#[5] Sair do programa

n1 = n2 = op = 0
print('Digite dois números')
n1 = int(input('Insira o primeiro'))
n2 = int(input('Agora o segundo'))
print('Escolha uma das opcoes')
print('---------------------')
print('[1] Somar')
print('{2} Multiplicar')
print('[3] Maior')
print('[4] Novos números')
print('[5] Sair do programa')
print('----------------------')
op = int(input())
while op != 5:
    if op == 1:
        print(f'A soma dos números é {n1+n2}')
        op = int(input('Escolha outra opçcao'))
    if op == 2:
        print(f'A multiplicação dos dois números é: {n1*n2}')
        op = int(input('Escolha outra opçcao'))
    if op == 3:
        if n1 > n2:
            print(f'O {n1} é maior que o {n2}')
            op = int(input('Escolha outra opçcao'))
        else:
            print(f'O {n2} é maior que o {n1}')
            op = int(input('Escolha outra opçcao'))
    if op == 4:
        print('Insira novos números')
        n1 = int(input('Insira o primeiro'))
        n2 = int(input('Agora o segundo'))
        op = int(input('Escolha outra opçcao'))
    if op == 5:
        print('Fim da aplicação')