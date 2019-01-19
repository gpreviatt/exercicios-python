#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
r1 = float(input('Digite o comprimento da Reta 1 '))
r2 = float(input('Digite o comprimento da Reta 2 '))
r3 = float(input('Digite o comprimento da Reta 3 '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo')
else:
    print('Os segmentos acima NÃO podem formar um triângulo')
