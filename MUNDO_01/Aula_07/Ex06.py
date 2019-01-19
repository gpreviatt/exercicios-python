#crie um algoritmo que leia um número e mostre o seu dobro triplo e raiz quadrada
import math
n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raiz = math.sqrt(n)
print('O dobro de {} é: {} o triplo é: {} e a raiz quadrada é: {:.1f} '.format(n, dobro, triplo, raiz))