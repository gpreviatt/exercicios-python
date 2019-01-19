#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
n = int(input('Digite um numero de 0 a 9999 '))

#desta forma ele pega sempre a particionar o numero pegando só a parte da casa decimal e guardar em uma variavel separada a vantagem é que se a alguma unidade for 0 ou nula ele guarda 0 no lugar e não gera erro
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('''                Milhar:{}
                Centena:{}
                Dezena:{}
                Unidade:{}'''.format(m, c, d, u))