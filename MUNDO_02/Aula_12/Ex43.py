# Desenvolva uma lógia que leia o peso e a altura de uma pessoa, Calculo seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - ABAIXO de 18.5: ABAIXO DO PESO
# - ENTRE 18.5 e 25: PESO IDEAL
# - ENTRE 25 e 30: SOBREPESO
# - ENTRE 30 e 40: OBESIDADE
# - ACIMA DE 40: OBESIDADE MORBIDA
import math
def printIMC (peso,altura,imc,calcImc):
    print('\n\033[34m O seu peso é de: {} e sua altura é de {} seu IMC é {:.2f} portanto você está na faixa de {}'.format(peso,altura,calcImc,imc))

peso = float(input('Digite seu peso '))
altura = float(input('Digite sua altura '))
imc = ''
calcImc = peso / altura ** 2
if calcImc <= 18.5:
    imc = 'ABAIXO DO PESO'
    printIMC(peso,altura,imc,calcImc)
if calcImc > 18.5 and calcImc <= 25:
    imc = 'PESO IDEAL'
    printIMC(peso,altura,imc,calcImc)
if calcImc > 25 and calcImc <= 30:
    imc = 'SOBREPESO'
    printIMC(peso,altura,imc,calcImc)
if calcImc > 30 and calcImc <= 40:
    imc = 'OBESIDADE'
    printIMC(peso,altura,imc,calcImc)
if calcImc > 40:
    imc = '\033[034m OBESIDADE MORBIDA'
    printIMC(peso,altura,imc,calcImc)
