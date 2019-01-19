# faca um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 ate 0, com uma pause de 1 segundo entre eles
import time
for c in range(10, 0, -1):
    time.sleep(1)
    if c==3:
        print('Contagem regressiva')
    print(c)
print(' *** Fogos estourando! ***')