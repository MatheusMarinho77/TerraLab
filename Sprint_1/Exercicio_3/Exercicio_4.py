#Exercicio 4 que pede ao usuario para digitar 


print('------Bem vindo ao programa que informa qual tipo foi digitado no teclado.\n------')
tipo = input('Digite algo para verificarmos:')
print('O {} é do tipo AlphaNumerico? '.format(tipo),tipo.isalnum())
print('O {} é do tipo Alpha(Letra)? '.format(tipo),tipo.isalpha())
print('{} esta somente com letras minusculas? '.format(tipo),tipo.islower())
print('O {} é do tipo Titulo(ou seja primeira letra maiuscula)? '.format(tipo),tipo.istitle())
