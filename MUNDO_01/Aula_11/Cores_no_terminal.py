#Arquivo com demonstração das cores no terminal
#Codigo anci
# \033[STYLE(normal,negrito,sublinhado);TEXT(cor);BACKGROUND(cor do fundo)m

#ESTILO DO TEXTO
print('\033[1m Negrito')
print('\033[4m Sublinhado\n')
print('\033[7m Inversão de cores')

#TEXTO
print('\033[30m Branco')
print('\033[31m Vermelho')
print('\033[32m Verde')
print('\033[33m Amarelo')
print('\033[34m Azul')
print('\033[35m Roxo')
print('\033[36m Azul Claro')
print('\033[37m Cinza')

#BACKGROUNDS
print('\033[40m Fundo Branco')
print('\033[41m Fundo Vermelho')
print('\033[42m Fundo Verde')
print('\033[43m Fundo Amarelo')
print('\033[44m Fundo Azul')
print('\033[45m Fundo Roxo')
print('\033[46m Fundo Azul Claro')
print('\033[47m Fundo Cinza')

print('\033[m') #volta a cor ao padrão normal

#para juntar os estilo basta colocar um ponto e virgula ex:
print('\033[4;31;44m  TESTE') #sempre nessa ordem estilo,texto,background
