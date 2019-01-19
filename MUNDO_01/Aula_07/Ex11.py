#Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária para pintá-la sabendo que cada litro de tinta pinta uma área de 2 metros

larg = float(input('Digite a largura na parede: '))
alt = float(input('Digite a altura da parede: '))
print('Sua parede tem a dimensão de {}X{} e sua área é de: {}'.format(larg, alt, larg*alt))
print('Você vai precisar para pintar essa parede {:.1f} litros de tinta'.format((larg*alt)/2))