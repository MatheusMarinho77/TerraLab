print('PROGRAMA DE SOMADORES DE NUMEROS INTEIRO')
somaPares = int(0)

for contador in range(0,6):
    numeroInformado = int(input('Informe um numero inteiro:'))
    if numeroInformado % 2 == 0:
        somaPares += numeroInformado

print('A soma final dos numeros pares informados durante o programa é: {}'.format(somaPares))