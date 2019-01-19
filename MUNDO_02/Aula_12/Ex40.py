#crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida, média abaixo de 5.0 REPROVADO, média entre 5.0 e 6.9 RECUPERAÇÃO média 7.0 ou superior APROVADO

n1 = float(input('Digite a nota do primeiro bimestre '))
n2 = float(input('Digite a nota do segundo bimestre '))

med = (n1+n2)/2
if med <= 5.0:
    print('\033[031m sua media final foi {} e você está REPROVADO'.format(med))
if med> 5.0 and med < 6.9:
    print('\033[033m sua media final foi {} e você está de RECUPERAÇÃO'.format(med))
if med >= 7.0:
    print('\033[034m sua media final foi {} e você está APROVADO!'.format(med))