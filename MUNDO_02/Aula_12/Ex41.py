#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade
# - até 9 anos: Mirim
# - até 14 anos: Infantil
# - até 19 anos: Junior
# - até 20 anos: Sênior
# - acima de 20 anos: Master

from datetime import datetime

def categoria(idade,cat):
    print('\033[034mVocê tem {} anos Sua categoria é: {}'.format(idade,cat))
cat = ''
anoAtual = datetime.now()
anosNasc = int(input('Digite seu ano de nascimento por favor: '))
idade = anoAtual.year - anosNasc

if idade <= 9:
    categoria(idade,'MIRIM')
if idade > 9 and idade <= 14:
    categoria(idade,'INFANTIL')
if idade > 14 and idade <= 19:
    categoria(idade,'Junior')
if idade > 19 and idade <= 20:
    categoria(idade,'SÊNIOR')
if idade > 20:
    categoria(idade,'MASTER')

