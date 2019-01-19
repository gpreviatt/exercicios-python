#crie um programa que leia o nome de uma pessoa e diga se ela tem 'silva' no nome
nome = str(input('Digite o nome de uma pessoa')).lower().strip()
print('A/O {} tem Silva no nome? [True/False] {} '.format(nome, 'silva' in nome)) #Este operador do python verifica se contem a string no caso 'silva' dentro da string nome