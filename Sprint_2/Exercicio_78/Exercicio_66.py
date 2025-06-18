numeroInformado = 0
soma = 0
contador = 0

while numeroInformado != 999:
    numeroInformado = int(input('DIGITE UM VALOR (999 PARA SAIR DO PROGRAMA): '))
    if numeroInformado == 999:
        break
    soma += numeroInformado
    contador += 1

print(f'NUMEROS INFORMADO {contador}')
print(f'SOMA DOS NUMEROS {soma}')    