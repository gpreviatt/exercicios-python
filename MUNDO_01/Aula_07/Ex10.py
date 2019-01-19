#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
dindin = float(input('Digite quantos reais você tem: '))
dolar = dindin / 3.27
print('Você tem R$: {} reais e pode comprar US: {:.2f} dolares'.format(dindin, dolar))