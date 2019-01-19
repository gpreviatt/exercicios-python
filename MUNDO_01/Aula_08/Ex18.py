#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import sin, cos, tan
ang = int(input('Digite o angulo: '))
print('O seno do ângulo vale: {:.2f} o cosseno: {:.2f} e a tangente: {:.2f}'.format(sin(ang), cos(ang), tan(ang)))