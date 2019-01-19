#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome SANTO
cidade = str(input('Digite o nome da cidade')).strip().lower()
print('A cidade {} começa com santo? [True/False]'.format(cidade))
print(cidade[:5] == 'santo') #pega do começo até o 5 caracter e verifica se possui o nome santo