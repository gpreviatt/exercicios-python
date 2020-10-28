# Números da Mega-Sena

João sempre entrega no caixa da lotérica suas apostas com os seis números ordenados de maneira **crescente.Os números devem ter paridades alternadas. Ou seja, se o primeiro número for par, o segundo deve ser ímpar, o terceiro par e assim por diante**

**A soma dos 6 números da aposta não pode ser um número múltiplo de 7 ou 13.**

Seu programa receberá como entrada quatro números inteiros que representam os valores para o primeiro, terceiro, quarto e sexto número da aposta escolhida por João, respectivamente. Os quatro números da entrada serão fornecidos de maneira ordenada crescente. **Como saída, seu programa deve gerar as possíveis apostas para a Mega-Sena considerando as regras do João.** Além disso, as apostas devem ser geradas em **ordem lexicográfica**, conforme os exemplos abaixo.

## Teste 01
Entrada

```
1 3 40 42 
```

Saída

```
Primeiro: 01
Terceiro: 03
Quarto: 40
Sexto: 42
```

```
Lista de apostas:
01 - 02 - 03 - 40 - 41 - 42
```

## Teste 02

Entrada

```
8 12 35 39
```

Saída

```
Primeiro: 08
Terceiro: 12
Quarto: 35
Sexto: 39
```

```
Lista de apostas:
08 - 09 - 12 - 35 - 36 - 39
08 - 09 - 12 - 35 - 38 - 39
08 - 11 - 12 - 35 - 36 - 39
```

## Teste 03

Entrada

```
15 25 40 48
```

Saída

```
Primeiro: 15
Terceiro: 25
Quarto: 40
Sexto: 48
```

```
Lista de apostas:
15 - 16 - 25 - 40 - 41 - 48
15 - 16 - 25 - 40 - 43 - 48
15 - 16 - 25 - 40 - 47 - 48
15 - 18 - 25 - 40 - 41 - 48
15 - 18 - 25 - 40 - 45 - 48
15 - 18 - 25 - 40 - 47 - 48
15 - 20 - 25 - 40 - 43 - 48
15 - 20 - 25 - 40 - 45 - 48
15 - 22 - 25 - 40 - 41 - 48
15 - 22 - 25 - 40 - 43 - 48
15 - 22 - 25 - 40 - 47 - 48
15 - 24 - 25 - 40 - 41 - 48
15 - 24 - 25 - 40 - 45 - 48
15 - 24 - 25 - 40 - 47 - 48
```

## teste arq05

Entrada

```
9 13 26 36
```

Saida

```
Primeiro: 09
Terceiro: 13
Quarto: 26
Sexto: 36

```

```
Lista de apostas:
09 - 10 - 13 - 26 - 27 - 36
09 - 10 - 13 - 26 - 29 - 36
09 - 10 - 13 - 26 - 31 - 36
09 - 10 - 13 - 26 - 33 - 36
09 - 10 - 13 - 26 - 35 - 36
09 - 12 - 13 - 26 - 27 - 36
09 - 12 - 13 - 26 - 29 - 36
09 - 12 - 13 - 26 - 31 - 36
09 - 12 - 13 - 26 - 33 - 36
09 - 12 - 13 - 26 - 35 - 36
```

## Código Base

```python
print("Primeiro:", "{:02}".format(n1))
print("Terceiro:", "{:02}".format(n3))
print("Quarto:", "{:02}".format(n4))
print("Sexto:", "{:02}".format(n6))

print("Lista de apostas:")
print("{:02} - {:02} - {:02} - {:02} - {:02} - {:02}".format(n1, n2, n3, n4, n5, n6))
```