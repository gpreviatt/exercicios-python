#escreva um programa para aprovar o emprestimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado

casaVlr = float(input('Digite o valor total da casa: '))
salario = float(input('Digite o valor do seu salário: '))
anos = int(input('Em quantos anos quer pagar a casa?: '))
prestMens = casaVlr/anos
if prestMens  > salario * 0.3:
    print('O valor da prestação é de: {} que EXCEDE 30% do seu salario que é de {}'.format(prestMens,salario))
    print('EMPRESTIMO NEGADO')
else:
    print('O valor da prestação é de: {} que NÃO EXCEDE 30% do seu salario que é de {}'.format(prestMens,salario))
    print('EMPRESTIMO CONCEDIDO')