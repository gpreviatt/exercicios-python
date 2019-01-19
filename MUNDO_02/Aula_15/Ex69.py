#crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada. o programa deverá perguntar se o usuário
#quer ou não continuar no final mostre quantas pessoas tem mais de 18. Quantos homens foram cadastradores. Quantas mulheres
#tem menos de 20 anos

idade = 0
sex = continua = ''
contIdadeMaiorQue18 =0
contaSexoM = 0
contaIdadeF = 0

while True:
    idade = int(input('Digite sua idade'))
    if idade > 18:
        contIdadeMaiorQue18 += 1
    sex = input('Digite o SEXO [M/F]')
    if sex == 'm':
        contaSexoM += 1
    if (sex == 'f') and (idade < 20):
        contaIdadeF += 1

    continua = input('Deseja continuar? [s/n]')
    if continua == 'n':
        print('Pessoas maiores de 18: {}'.format(contIdadeMaiorQue18))
        print('Homens cadastrados: {}'.format(contaSexoM))
        print('Mulheres com menos de 20 anos: {}'.format(contaIdadeF))
        break

