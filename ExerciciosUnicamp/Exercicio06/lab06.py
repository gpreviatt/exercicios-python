###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - De Volta para o Passado
# Nome: 
# RA: 
###################################################

# Leitura de dados

n = int(input("Dias: "))
while n > 30:
    print("n = {} nao pode ser maior que 30 tente novamente".format(n))
    n = int(input())

valores = {}

dia_venda = 0
valor_venda = 0

for i in range(1, n + 1):
    valores[i] = float(input("Cotação: "))
    if valor_venda < valores[i]:
        valor_venda = valores[i]
        dia_venda = i

k = int(input("Diferença de Dias: "))
q = float(input("Total investido: "))

# Escolha da melhor variação de valores da ação

dia_compra = 0
valor_compra = 0


# Percorre a lista para ver qual o melhor dia de compra das ações
for i in range(1, dia_venda):
    if valores[i] < valor_compra or valor_compra == 0:
        valor_compra = valores[i]
        dia_compra = i
    if (dia_venda - dia_compra) == k:
        valor_compra = valores[i]
        dia_compra = i
        break

qtde_acoes = q / valor_compra
lucro = (qtde_acoes * valor_venda) - q

# Saída de dados

print('Dia da compra:', dia_compra)
print('Valor de compra: R$', format(valor_compra, '.2f').replace('.', ','))
print('Dia da venda:', dia_venda)
print('Valor de venda: R$', format(valor_venda, '.2f').replace('.', ','))
print('Quantidade de acoes compradas:', format(qtde_acoes, '.2f').replace('.', ','))
print('Lucro: R$', format(lucro, '.2f').replace('.', ','))