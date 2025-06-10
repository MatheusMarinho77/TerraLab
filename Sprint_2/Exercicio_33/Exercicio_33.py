# Programa que le 3 numeros e informa qual é o maior e qual é o menor

numero1 = int(input('Informe o valor do primeiro numero: '))
numero2 = int(input('Valor do segundo numero: '))
numero3 = int(input('Valor do terceiro numero: '))

maiorNumero = numero1
menorNumero = numero1

if numero2 > numero1:
    maiorNumero = numero2
if numero3 > maiorNumero:
    maiorNumero = numero3

print('---------O maior numero informado é {}--------- \n\n'.format(maiorNumero))

if numero2 < menorNumero:
    menorNumero = numero2
if numero3 < menorNumero:
    menorNumero = numero3

print('---------O menor numero informado é {}---------\n\n'.format(menorNumero))    
