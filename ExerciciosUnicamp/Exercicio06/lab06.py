###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - De Volta para o Passado
# Nome: 
# RA: 
###################################################

# Leitura de dados

n = int(input())
while n > 30:
    print("n = {} nao pode ser maior que 30 tente novamente".format(n))
    n = int(input())

valores = {}

dia_venda = 0
valor_venda = 0
valor_compra = 0.0
dia_compra = 1

for i in range(1, n + 1):
    valores[i] = float(input())
    if valor_compra > valores[i]:
        valor_compra = valores[i]
        dia_compra = i

k = int(input())
q = float(input())

# Escolha da melhor variação de valores da ação

for i in range(1, len(valores)):
    if valores[i] > valor_venda and dia_compra + i <= k :
        valor_venda = valores[i]
        dia_venda = i

qtde_acoes = int(q / valor_compra)
lucro = (valor_venda - valor_compra) * qtde_acoes

# Saída de dados

print('Dia da compra:', dia_compra)
print('Valor de compra: R$', format(valor_compra, '.2f').replace('.', ','))
print('Dia da venda:', dia_venda)
print('Valor de venda: R$', format(valor_venda, '.2f').replace('.', ','))
print('Quantidade de acoes compradas:', format(qtde_acoes, '.0f'))
print('Lucro: R$', format(lucro, '.2f').replace('.', ','))