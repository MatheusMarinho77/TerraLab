import math

print('PROGRAMA DE VERIFICAÇÃO DE NUMEROS PRIMOS')

numeroInformado = int(input('INFORME UM NUMERO INTEIRO:'))
primo = False

if numeroInformado > 1:
    primo = True
elif numeroInformado == 2:
    primo = True
elif numeroInformado % 2 == 0:
    if numeroInformado == 2 :
        primo = True
    primo = False


for i in range (1,numeroInformado):
    if numeroInformado % i == 0:
        primo = False

print('O numero {} é PRIMO? {}'.format(numeroInformado,primo))