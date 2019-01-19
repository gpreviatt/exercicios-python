# crie um programa que leia varios números inteiros pelo teclado, o programa só vai para quando o usuário digitar
# 999, que é a condição de parada. No final mostre quantos números foram digitados e a soma entre eles.

contValor = somValor = n = 0
while True: # while infinito
    n = int(input('Digite um número(999 para)'))
    if n == 999:
        break
    contValor += 1
    somValor += n
print('O resultado dos {} valores somados é: {}'.format(contValor, somValor))

