#Crie um programa que leia vários números inteiros pelo teclado. O programa
# só vai parar quando o usuário digitar o valor 999 que é a condição de parada
#No final mostre quantos números foram digitados e qual foi a soma entre eles desconsiderando o flag
n = int(input('Digite um número'))
total = 0
cont = 0
while n != 999:
    total += n
    if n != 999:
        n = int(input('Digite um número'))
    cont += 1
print(f' Foram digitados {cont} numeros e a soma deles é {total}')