#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade -se ele vai se alistar ao serviço militar , -se é hora de se alistar, se já passou o tempo de se alistar

from datetime import datetime
now = datetime.now() #pega o hora do sistema
nasc = int(input('Digite o seu ano de nascimento'))
anoDeNasc = now.year - nasc
if anoDeNasc >= 18 and anoDeNasc < 21:
    print('Você está com {} está na hora do alistamento'.format(anoDeNasc))
if anoDeNasc >= 21:
    print('Você está com {} ja passou da hora de se alistar'.format(anoDeNasc))
if anoDeNasc < 18:
    print('Você tem {} e ainda não tem idade para de alistar'.format(anoDeNasc))
