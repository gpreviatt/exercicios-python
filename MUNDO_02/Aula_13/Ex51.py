#desenvolva um programa que leia o primeiro termo e a razão de uma PA
#No final, mostre os 10 primeiros termos dessa progressão
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimoTermo = primeiro + (11-1) * razao
for c in range(primeiro,decimoTermo,razao):
    print(c)