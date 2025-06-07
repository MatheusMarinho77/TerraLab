## LER UM NUMERO REAL PELO TECLADO E MOSTRE A SUA POSIÇÃO INTEIRA

import math

numero = float(input('Informe um numero do conjunto dos numeros Reais:'))
print('O numero {} tem a parte inteira {}'.format(numero, math.trunc(numero)))