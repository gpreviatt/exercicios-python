# crie um programa que moste na tela todos numeros impares e multiplos de 3 no intervalo de 1 e 500
som = 0
for c in range(0, 500):
    if ((c % 3) == 0) and (((c*5)/5) == c):
        som +=1
print(som)


