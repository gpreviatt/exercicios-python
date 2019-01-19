#faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
salario = float(input('Digite seu salário: '))
print('Seu salário é de: R$:{:.2f} com o aumento de 15% vai para: R$: {:.2f}'.format(salario,salario+((salario/100)*15)))