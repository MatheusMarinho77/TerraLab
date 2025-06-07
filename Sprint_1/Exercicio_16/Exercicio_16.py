## LER UM NUMERO REAL PELO TECLADO E MOSTRE A SUA POSIÇÃO INTEIRA

from math import trunc

numero = float(input('Informe um numero do conjunto dos numeros Reais:'))

print('O numero {} tem a parte inteira {}'.format(numero, trunc(numero)))