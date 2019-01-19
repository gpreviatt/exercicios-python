#Elabora um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento:
#- A vista dinheiro/cheque: 10% de descibti
#- Em até 2x no cartão preço normal
#-3x ou mais no cartão 20% de juros

preco = float(input('Digite o preço do seu produto: '))
precoNovo = preco
print('''Escolha a forma de pagamento 
1. A vista Dinheiro/Cheque [10% DE DESCONTO]
2. Em 2x no cartão [PREÇO NORMAL]
3. 3x ou mais [20% DE JUROS]''')
opcao = int(input('Escolha agora! '))
if opcao == 1:
    precoNovo = preco - ((preco/100)*10)
if opcao == 3:
    precoNovo = preco + ((preco/100)*20)
print('Você vai pagar pelo produto R$: {:.2f}'.format(precoNovo))