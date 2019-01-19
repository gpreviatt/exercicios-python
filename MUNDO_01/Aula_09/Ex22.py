#crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todas as letras maiúsculas
# o nome com todas as letras minúsculas
# quantas letras ao todo (sem considerar espaços)
# quantas letras tem o primeiro nome
nome = input('Digite seu nome completo ')
print('Nome em maiúsculo {}'.format(nome.upper().strip()))
print('Nome em minúsculo {}'.format(nome.lower().strip()))
print('Quantidade de letras sem espaços: {}'.format(len(nome) - nome.count(' ')))
print('O primeiro nome tem {} letras'.format(nome.find(' ')))