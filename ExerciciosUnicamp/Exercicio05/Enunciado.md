# Números da Mega-Sena

João é um grande apostador da Mega-Sena. Toda semana ele dirige-se até a lotérica perto de sua casa com seus palpites e faz as apostas na esperança de um dia tornar-se milionário. Como grande parte dos apostadores da Mega-Sena, João tem supertições e segue algumas regras para definir os números de suas apostas, sendo elas:

João sempre entrega no caixa da lotérica suas apostas com os seis números ordenados de maneira crescente.
Os números devem ter paridades alternadas. Ou seja, se o primeiro número for par, o segundo deve ser ímpar, o terceiro par e assim por diante. Se o primeiro número for ímpar, o segundo deve ser par, o terceiro ímpar e assim por diante.
A soma dos 6 números da aposta não pode ser um número múltiplo de 7 ou 13.
João consegue dar bons palpites para o primeiro, terceiro, quarto e sexto número, mas sempre fica na dúvida em relação ao segundo e ao quinto número. Sabendo das suas habilidades com programação, João pediu sua ajuda. Você deve fazer um programa que gere todas as possíveis apostas considerando que João irá fornecer para você o primeiro, terceiro, quarto e sexto número. Além disso, você deve considerar as regras estabelecidas para a escolha e exibição dos números das apostas.

Seu programa receberá como entrada quatro números inteiros que representam os valores para o primeiro, terceiro, quarto e sexto número da aposta escolhida por João, respectivamente. Os quatro números da entrada serão fornecidos de maneira ordenada crescente. Como saída, seu programa deve gerar as possíveis apostas para a Mega-Sena considerando as regras do João. Além disso, as apostas devem ser geradas em ordem lexicográfica, conforme os exemplos abaixo.

Exemplos de entradas e saídas esperadas pelo seu programa:

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

## Código Base
No arquivo auxiliar lab05.py você irá encontrar um código base para dar início ao processo de elaboração dessa tarefa. Além disso, nele você encontrará a formatação para exibir os seis números de uma aposta com dois dígitos cada:

```python
print("Primeiro:", "{:02}".format(n1))
print("Terceiro:", "{:02}".format(n3))
print("Quarto:", "{:02}".format(n4))
print("Sexto:", "{:02}".format(n6))

print("Lista de apostas:")
print("{:02} - {:02} - {:02} - {:02} - {:02} - {:02}".format(n1, n2, n3, n4, n5, n6))
```

## Orientações

Veja aqui a página de submissão da tarefa.
O arquivo a ser submetido deve se chamar lab05.py.
No link "Arquivos auxiliares" há um arquivo compactado (aux05.zip) que contém todos os arquivos de testes abertos (entradas e saídas esperadas).
O laboratório é composto de 10 testes abertos e 10 testes fechados.
O limite máximo será de 20 submissões.
Acesse o sistema SuSy com seu RA (apenas números) e a senha que você utiliza para fazer acesso ao sistema da DAC.
Você deve seguir as instruções de submissão descritas no enunciado.
Serão considerados apenas os resultados da última submissão.
Esta tarefa tem peso 1.
O prazo final para submissão é dia 08/11/2020 (domingo).