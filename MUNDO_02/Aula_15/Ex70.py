#crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar e no final mostre:
#qual é o total gasto na compra. Quantos produtos custam mais de R$: 1000,00. Qual é o nome do produto mais barato

nomeProduto = ''
valorProduto = 0.0
contaTotalCompra = 0.0
contaMaisDeMil = 0
nomeProdutoMaisBarato = ' '
nomeAnterior = ' '
valorAnterior = 0.0
guardaNomeMaisBarato = ' '
continua = ''
while True:
    valorAnterior = valorProduto
    nomeProduto = input('Digite o nome do produto')
    valorProduto = float(input('Digite o valor do produto'))
    contaTotalCompra += valorProduto

    if valorProduto > 1000:
        contaMaisDeMil += 1

    if valorProduto < valorAnterior:
        nomeAnterior = nomeProduto

    continua = input('Deseja continuar [s/n]')
    if continua == 'n':
        print('O total gasto na compra foi de: {}'.format(contaTotalCompra))
        print('{} Produtos custam mais caro que R$: 1.000,00'.format(contaMaisDeMil))
        print('O nome do produto mais barato é: {}'.format(nomeAnterior))
        break