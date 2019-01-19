#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os
#n primeiros elementos de uma sequencia de Fibonacci

print('*'*30)
print('Sequencia de Fibonacci')
print('*'*30)
n = int(input('Digite a quantidade de termos que deseja ver'))
t1 = 0
t2 = 1
cont = 3
print(f'{t1} - {t2} - ',end='')
while cont <= n:
    t3 = t1 + t2
    print(f'{t3}- ', end='')
    t1 = t2
    t2 = t3
    cont+= 1



