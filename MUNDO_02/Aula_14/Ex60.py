#faça um programa que leia um número qualquer e mostre seu fatorial

n = int(input('Digite o numero do fatorial'))
cont = 1
fat = 1
while cont <= n:
    fat = fat * cont
    cont = cont + 1
print(f'o fatorial de {n} é: {fat}')
