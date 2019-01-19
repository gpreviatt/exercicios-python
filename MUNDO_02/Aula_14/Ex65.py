# Crie um programa que leia vários números inteiros pelo teclado.
# No fimal da execução mostre a médis entre todos os valores e qual
# foi o maior e o menor valores lidos. O programa deve perguntar
# ao usuário se ele quer ou não continuar a digitar valores

tot = menor = maior = cont = 0
continua = 'S'
while continua in 'Ss':
    n = int(input('Digite um número'))
    tot += n
    cont += 1
    if cont == 1: #no começo o cont é igual isso serve para o menor não ser sempre o zero
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continua = str(input('Deseja Continua [S/N]?')).upper().strip()
print(f'A média entre os valores foi {tot/cont} o maior foi {maior} e o menor foi {menor}')
