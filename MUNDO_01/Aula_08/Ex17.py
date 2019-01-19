#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
from math import hypot
opost = float(input('Digite o cateto oposto do triângulo: '))
adjacent = float(input('Digite o cateto adjacente do triângulo: '))
print('A hypotenusa do triangulo retângulo vale: {:.2f}'.format(hypot(opost,adjacent)))