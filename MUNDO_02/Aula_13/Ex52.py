#faça um programa que leia um número inteiro e diga se ele é ou não um número primo
n = int(input('Digite um numero '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
       print('\033[36m',end='') #coloca cor verde na letra
       tot+=1
    else:
        print('\033[31m',end='') #coloca cor vermelha na letra
    print('{} '.format(c), end=' ')
print('\no numero {} é divisivel {} vezes'.format(n,tot))
print('\033[m') #remove a formatação de for
if tot == 2:
    print('O numero {} É PRIMO'.format(n))
else:
    print('O numero {} NÃO É PRIMO'.format(n))
