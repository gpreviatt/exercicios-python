# De Volta para o Passado

Primeiramente, o seu programa receberá um valor N, indicando o número de dias que você tem registro do preço das ações, sendo que N sempre será menor ou igual a 30. Nas próximas N linhas, serão lidos os preços diários das ações. Na sequência, será lido um valor K, indicando o número máximo de dias permitido entre a compra e venda da ação. Por fim, o seu programa deverá ler um valor Q, indicando a quantidade de dinheiro que você levará na viagem.

Você deverá comprar ações em um único dia e deverá vender ações em um único dia, de modo que tenha o maior lucro possível. As ações são vendidas por inteiro, ou seja, não é possível comprar partes de uma ação. Você deve sempre comprar a maior quantidade possível de ações.

A saída deverá conter o dia e o valor de compra de cada ação, o dia e valor de venda de cada ação, a quantidade de ações compradas e o lucro total obtido. Em caso de empate, deverá ser escolhido o menor dia de compra e o menor dia de venda.

## Teste 01

Entrada

```
10
12.55
13.32
15.13
15.65
16.37
20.90
15.21
13.88
11.45
10.50
2
5000.00
```

Saída

```
Dia da compra: 4
Valor de compra: R$ 15,65
Dia da venda: 6
Valor de venda: R$ 20,90
Quantidade de acoes compradas: 319
Lucro: R$ 1674,75
```

## Teste 02
Entrada

```
10
12.55
13.32
15.13
15.65
16.37
20.90
15.21
13.88
11.45
10.50
5
10000.00
```

Saída

```
Dia da compra: 1
Valor de compra: R$ 12,55
Dia da venda: 6
Valor de venda: R$ 20,90
Quantidade de acoes compradas: 796
Lucro: R$ 6646,60
```

## Teste 03

Entrada

```
6
6.55
6.54
6.53
6.52
6.51
6.50
5
2000.00
```

Saída

```
Dia da compra: 1
Valor de compra: R$ 6,55
Dia da venda: 1
Valor de venda: R$ 6,55
Quantidade de acoes compradas: 305
Lucro: R$ 0,00
```

## Código Base

No arquivo auxiliar lab06.py você irá encontrar um código base para dar início ao processo de elaboração deste laboratório. Nesse arquivo, você encontrará a formatação para exibir o dia da compra, o valor da compra (com duas casas decimais), o dia da venda, o valor da venda (com duas casas decimais), a quantidade de ações compradas e o lucro obtido (com duas casas decimais):

```python
print('Dia da compra:', dia_compra)
print('Valor de compra: R$', format(valor_compra, '.2f').replace('.', ','))
print('Dia da venda:', dia_venda)
print('Valor de venda: R$', format(valor_venda, '.2f').replace('.', ','))
print('Quantidade de acoes compradas:', qtde_acoes)
print('Lucro: R$', format(lucro, '.2f').replace('.', ','))
```

## Orientações
Veja aqui a página de submissão da tarefa.
O arquivo a ser submetido deve se chamar lab06.py.
No link "Arquivos auxiliares" há um arquivo compactado (aux06.zip) que contém todos os arquivos de testes abertos (entradas e saídas esperadas).
O laboratório é composto de 10 testes abertos e 10 testes fechados.
O limite máximo será de 20 submissões.
Acesse o sistema SuSy com seu RA (apenas números) e a senha que você utiliza para fazer acesso ao sistema da DAC.
Você deve seguir as instruções de submissão descritas no enunciado.
Serão considerados apenas os resultados da última submissão.
Esta tarefa tem peso 2.
O prazo final para submissão é dia 15/11/2020 (domingo).