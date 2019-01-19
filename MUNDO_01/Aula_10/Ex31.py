#Desenvolva um programa que pergunte a distnacia de uma viagem em km. Calcule o preço da passagem, cobrando R$: 0.50 por km para viagens de até 200km e R$: 0.45 para viagens mais longas
distancia = int(input('Digite a distância da viagem em Km/h: '))
preco = 0.0
valor = 0.0
if distancia > 200:
    valor = 0.45
    preco = distancia * 0.45
else:
    valor = 0.50
    preco = distancia * 0.50
print('O valor da viagem foi de R$: {} e o praço cobrado por quilimetro foi de R$: {}'.format(preco, valor))