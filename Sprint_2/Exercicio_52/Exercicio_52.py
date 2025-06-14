import math

print('PROGRAMA DE VERIFICAÇÃO DE NUMEROS PRIMOS')
numeroInformado = int(input('INFORME UM NUMERO INTEIRO:'))
primo = True

for i in range(2,numeroInformado - 1):
    if numeroInformado % i == 0:
        if numeroInformado == 1:
            primo = True
            continue
        elif numeroInformado == 2:
            primo = True
        primo = False
        break

print('O numero {} é primo???\n{}'.format(numeroInformado,primo))
