#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas suas informações possiveis
algo = input('Digite algo: ')
print('É um número? {}'.format(algo.isnumeric()))
print('É alfabético? {}'.format(algo.isalpha()))
print('É alfanúmerico? {}'.format(algo.isalnum()))
print('É um caracter decimal? {}'.format(algo.isdecimal()))
print('Todos os caracteres estão em mínusculo? {}'.format(algo.islower()))
print('Todos os caracteres estão em maíusculo? {}'.format(algo.isupper()))
print('Existem apenas espaços em branco? {}'.format(algo.isspace()))
print('Pode ser impresso? {}'.format(algo.isprintable()))
