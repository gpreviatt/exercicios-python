#faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
produto = float(input('Digite o valor do produto '))
print('O produto de valor R$:{:.2f} com 5% de desconto é: R$:{:.2f}'.format(produto, produto - ((produto/100) * 5)))