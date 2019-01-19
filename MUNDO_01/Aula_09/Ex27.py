#faça um programa que leia o nome de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
# Ex Ana maria de Souza primeiro = Ana ultimo = Souza
nome = str(input('Digite seu nome completo: ')).strip()
lista = nome.split() #divide em uma lista a string
print('Primeiro: {}'.format(lista[0]))
print('Ultimo: {}'.format(lista[len(lista)-1])) #aqui estamos pegando o tamanho da lista e tirando 1 porque a contagem vai de zero até o tamanho-1