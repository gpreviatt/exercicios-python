# desenvolva um programa que leia seis numeros inteiros e mostre apenas daquelas que forem pares. Se o valor digitado for impar desconsidere-0
som = 0
for c in range(1, 7):
    n = int(input('Digite um n'))
    if (n % 2) == 0:
       som += n
print('A soma dos valores pares foi: {}'.format(som))