###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Números da Mega-Sena
# Nome:
# RA: 
###################################################

# Leitura de dados

# n1 = int(input())
# n2 = n1
# n3 = int(input())
# n4 = int(input())
# n5 = n4
# n6 = int(input())

# teste 01
# n1 = 1
# n3 = 3
# n4 = 40
# n6 = 42

# teste 02
# n1 = 8
# n3 = 12
# n4 = 35
# n6 = 39

# teste 03
n1 = 15
n3 = 25
n4 = 40
n6 = 48

# test arq 05
# n1 = 9
# n3 = 13
# n4 = 26
# n6 = 36

# Impressão dos quatro números fornecidos como entrada

print("Primeiro:", "{:02}".format(n1))
print("Terceiro:", "{:02}".format(n3))
print("Quarto:", "{:02}".format(n4))
print("Sexto:", "{:02}".format(n6))

# Processamento e impressão da lista de possíveis apostas

print("Lista de apostas:")

for i in range(n1,n3):
    n5 = n4
    if (n1%2 == 0 and i%2 == 0) or (n1%2 != 0 and i%2 != 0):
        continue
    else:
        n2 = i
    for n in range(n4, n6):
        if (n4%2 == 0 and n%2 == 0) or (n4%2 != 0 and n%2 != 0):
            continue
        n5 = n

        # Verifica se a somatoria dos numeros NÃO é um multiplo de 7 ou 13
        sum = n1 + n2 + n3 + n4 + n5
        if (sum%7) and (sum%13):
            print("{:02} - {:02} - {:02} - {:02} - {:02} - {:02}".format(n1, n2, n3, n4, n5, n6))
