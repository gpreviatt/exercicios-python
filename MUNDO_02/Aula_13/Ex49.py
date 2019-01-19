# refaca o desafio 9 mostrando a tabuada do numero que o usuario escolher so que agora com o laco for
n = int(input('Digite um numero'))
for c in range(0, 11):
    print('{} x {} = {}'.format(n,c,(c*n)))