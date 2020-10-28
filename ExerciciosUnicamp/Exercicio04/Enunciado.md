# Street Fighter

Neste laboratório, você deve simular uma luta entre Ryu e Ken, informando no fim qual dos dois lutadores saiu vitorioso.

Cada lutador começa a luta com uma quantidade de pontos de vida **(hp, do inglês Health Points)** e realiza uma sequência de golpes que geram decréscimo no hp do adversário. Inicialmente, seu programa deve ler dois valores inteiros que indicam a quantidade inicial de hp dos lutadores Ryu e Ken, respectivamente. Depois disso, você deve ler a sequência de golpes que foram realizados na luta. **Um golpe é um valor inteiro, sendo que um golpe com valor positivo indica que o golpe foi realizado pelo lutador Ryu e um golpe com valor negativo indica que o golpe foi realizado pelo lutador Ken. O valor absoluto de um golpe indica a quantidade que deve ser diminuída do hp do adversário. Para cada golpe, você deve imprimir três linhas de informações. A primeira linha deve informar quem aplicou o golpe e o valor absoluto do mesmo. A segunda e terceira linha devem informar o hp dos lutadores Ryu e Ken, respectivamente.** Exemplo das informações que devem ser exibidas para cada golpe aplicado:

```
<Lutador que atacou> APLICOU UM GOLPE: <Valor absoluto do golpe>
HP RYU = <HP do lutador RYU>
HP KEN = <HP do lutador KEN>
```

O hp de cada lutador nunca será negativo, sendo que seu valor mínimo é zero. No momento que o hp de um dos lutadores chega em zero o mesmo é considerado como derrotado e a luta é encerrada. Seu programa deve imprimir o nome do lutador que venceu a luta seguido do número de golpes aplicados por cada lutador no seguinte formato:

```
LUTADOR VENCEDOR: <Lutador vencedor>
GOLPES RYU = <Número de golpes aplicados pelo lutador RYU>
GOLPES KEN = <Número de golpes aplicados pelo lutador KEN>
Exemplos de entradas e saídas esperadas pelo seu programa:
```

## Teste 01

Entrada

```
80 50 15 -15 20 -20 15
```

Saída

```
RYU APLICOU UM GOLPE: 15
HP RYU = 80
HP KEN = 35
KEN APLICOU UM GOLPE: 15
HP RYU = 65
HP KEN = 35
RYU APLICOU UM GOLPE: 20
HP RYU = 65
HP KEN = 15
KEN APLICOU UM GOLPE: 20
HP RYU = 45
HP KEN = 15
RYU APLICOU UM GOLPE: 15
HP RYU = 45
HP KEN = 0
LUTADOR VENCEDOR: RYU
GOLPES RYU = 3
GOLPES KEN = 2
```

## Teste 02
Entrada

```
70 80 -20 15 -15 -20 20 15 10 -20
```

Saída

```
KEN APLICOU UM GOLPE: 20
HP RYU = 50
HP KEN = 80
RYU APLICOU UM GOLPE: 15
HP RYU = 50
HP KEN = 65
KEN APLICOU UM GOLPE: 15
HP RYU = 35
HP KEN = 65
KEN APLICOU UM GOLPE: 20
HP RYU = 15
HP KEN = 65
RYU APLICOU UM GOLPE: 20
HP RYU = 15
HP KEN = 45
RYU APLICOU UM GOLPE: 15
HP RYU = 15
HP KEN = 30
RYU APLICOU UM GOLPE: 10
HP RYU = 15
HP KEN = 20
KEN APLICOU UM GOLPE: 20
HP RYU = 0
HP KEN = 20
LUTADOR VENCEDOR: KEN
GOLPES RYU = 4
GOLPES KEN = 4
```

## Teste 03

Entrada

```
90 60 15 15 -10 10 10 10
```

Saída

```
RYU APLICOU UM GOLPE: 15
HP RYU = 90
HP KEN = 45
RYU APLICOU UM GOLPE: 15
HP RYU = 90
HP KEN = 30
KEN APLICOU UM GOLPE: 10
HP RYU = 80
HP KEN = 30
RYU APLICOU UM GOLPE: 10
HP RYU = 80
HP KEN = 20
RYU APLICOU UM GOLPE: 10
HP RYU = 80
HP KEN = 10
RYU APLICOU UM GOLPE: 10
HP RYU = 80
HP KEN = 0
LUTADOR VENCEDOR: RYU
GOLPES RYU = 5
GOLPES KEN = 1
```