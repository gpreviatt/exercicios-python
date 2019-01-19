#Escreva um programa que leia a velocidade de um carro. Se ele utrapassar 80km/h. mostre uma mensagem dizendo que ele foi multado a multa vai custar R$: 7 reias por cada km acima do limite
velocidade = int(input('Qual sua velocidade KM/h ?: '))
if velocidade > 80:
    print('VOCÊ FOI MULTADO')
    multa = float((velocidade - 80) * 7)
    print('A multa vai custar R$: {:.2f}'.format(multa))
else:
    print('PARABÉNS você não utrapassou o limite de velocidade')