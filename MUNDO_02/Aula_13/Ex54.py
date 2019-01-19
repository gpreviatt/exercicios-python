#faça um programa que leia a idade de 7 pessoas e diga quantas delas ainda não atingiram a maioridade e quantas são maiores de idade
maior=menor=0
for c in range(1,8):
    idade = int(input(f'{c}° Pessoa qual sua idade'))
    if idade >= 18:
        maior +=1
    if idade < 18:
        menor+=1
print('{} pessoas são maiores idade e \n {} sao menores de idade'.format(maior,menor))