#faça um programa que leia o peso de 5 pessoas. No final mostre qual foi o maior e qual foi o menor peso lido
menor = maior =0.0
for c in range(1,6):
    peso = float(input('Qual seu peso?'))
    if c == 1:
        menor = maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('{} Kg foi o maior peso \n{} Kg foi o menor peso'.format(maior,menor))