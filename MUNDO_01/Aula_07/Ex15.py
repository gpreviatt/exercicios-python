#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelo quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$: 60.00 por dia e R$: 0.15 por KM rodado.
percorrido = float(input('Quantos Quilometros(KM) foram percorridos? '))
dias = int(input('Quantos dias você ficou com o carro: '))
precoPagar = (dias * 60) + (percorrido * 0.15)
print('Você percorreu {} KM em {} dias portanto você deve pagar R$: {}'.format(percorrido,dias,precoPagar))