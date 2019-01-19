#faça um programa que leia o sexo de uma pessoa, mais só aceite os valores 'm' ou 'f'
#caso esteja errado, peça a digitação novamente até ter um valor correto
sexo = str(input('Digite o Sexo[M/F]')).strip().upper()
while sexo not in 'MmFf':
    sexo = str(input('Opção invalida, por favor digite uma opção valida'))
print(f'O Sexo {sexo} foi inserido')
