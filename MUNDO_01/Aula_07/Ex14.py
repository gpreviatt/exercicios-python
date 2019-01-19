#Escreva um programa que converta uma temperatura digitada em Celsius(c) para Fahrenheit(f)
c = float(input('Digite a temperatura em Celcius: '))
f = ((9*c)/5)+32 #formula geral
print('A temperatura em Celsius de: {} é {} em Fahrenheit'.format(c, f))
