#Refaça o DESAFIO 35 dos triângulos acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilatero: todos os lados iguais
# - Isosceles: Dois lados iguais
# - Escaleno: todos os lados diferentes

l1 = int(input('Digite o lado 1'))
l2 = int(input('Digite o lado 2'))
l3 = int(input('Digite o lado 3'))

if l1 == l2 == l3:
    print('O triângulo é EQUILÁTERO')
if (l1 == l2) or (l1 == l3) or (l2 == l3):
    print('O triângulo é ISÓCELES')
if(l1 != l2) or (l1 != l3) or (l2 != l3):
    print('O triângulo é Escaleno')