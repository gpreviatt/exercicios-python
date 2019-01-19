#melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais
#alguns termos. O programa encerra quando disse que quer mostrar 0 termos

n = int(input('Digite um número: '))
r = int(input('Digite a razão: '))
termo = n
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont<= total:
        print(termo)
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Deseja ver mais quantos termos? '))
print(f'Foram mostrados {total} termos')

