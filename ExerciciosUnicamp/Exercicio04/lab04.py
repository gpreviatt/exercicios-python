###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Street Fighter
# Nome:
# RA: 
###################################################

# Leitura do hp dos lutadores
ryuHp = int(input())
kenHp = int(input())

# Leitura da sequência de golpes
golpesRyu = 0
golpesKen = 0
vencedor = ""
while ryuHp > 0 and kenHp > 0:
    golpe = int(input())
    if golpe > 0:
        kenHp = kenHp - golpe
        golpesRyu = golpesRyu + 1
        print("RYU APLICOU UM GOLPE:", golpe)

        if kenHp <= 0:
            kenHp = 0
            vencedor = "RYU"
    else:
        golpe = -golpe
        ryuHp = ryuHp - golpe
        golpesKen = golpesKen + 1

        print("KEN APLICOU UM GOLPE:", golpe)
        if ryuHp <= 0:
            ryuHp = 0
            vencedor = "KEN"

    print("HP RYU =", ryuHp)
    print("HP KEN =", kenHp)

# Impressão do vencedor e do número de golpes aplicados
print('LUTADOR VENCEDOR:', vencedor)
print('GOLPRES RYU =' , golpesRyu)
print('GOLPRES KEN =', golpesKen)