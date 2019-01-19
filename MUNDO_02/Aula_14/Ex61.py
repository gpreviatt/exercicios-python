#refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA
#mostrando os 10 primeiros termos da progressão usando  a estrutura while

n = int(input('Digite um número: '))
r = int(input('Digite a razão: '))
decimoTermo = n + (11 - 1) * r
while n < decimoTermo:
    print(n)
    n = n + r
