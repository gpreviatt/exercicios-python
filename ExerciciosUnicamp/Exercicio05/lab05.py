###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Números da Mega-Sena
# Nome:
# RA: 
###################################################

# Leitura de dados

n1 = int(input())
n3 = int(input())
n4 = int(input())
n6 = int(input())

# Impressão dos quatro números fornecidos como entrada

print("Primeiro:", "{:02}".format(n1))
print("Terceiro:", "{:02}".format(n3))
print("Quarto:", "{:02}".format(n4))
print("Sexto:", "{:02}".format(n6))

# Processamento e impressão da lista de possíveis apostas

print("Lista de apostas:")

for i in range(n1,n3):
    # regra impar ou par
    if (n1%2 and i%2) or (not n1%2 and not i%2):
        continue
    n2 = i
    n5 = n4
    for n in range(n4, n6):
        # regra par ou impar
        if (n4%2 and n%2) or (not n4%2 and not n%2):
            continue
        n5 = n

        # exibe se a somatoria dos numeros NÃO é um multiplo de 7 ou 13
        sum = n1 + n2 + n3 + n4 + n5 + n6
        if (sum%7) and (sum%13):
            print("{:02} - {:02} - {:02} - {:02} - {:02} - {:02}".format(n1, n2, n3, n4, n5, n6))
