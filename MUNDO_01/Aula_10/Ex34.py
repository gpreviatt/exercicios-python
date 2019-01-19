#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
#para salários superiores a R$: 1,250.00, calcule um aumento de 10%
#para os inferiores ou iguais, o aumento é de 15%
salario = float(input('Digite seu salário: '))
porcentagem = ''
if salario > 1250:
    novoSalario = salario + ((salario/100)*10)
    porcentagem = '10%'
else:
    novoSalario = salario + ((salario/100)*15)
    porcentagem = '15%'
print('Seu novo salário teve um aumento de {} e é de: {}'.format(porcentagem, novoSalario))