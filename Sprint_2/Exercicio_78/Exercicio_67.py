numeroInformado = 0

print('\n\n---------BEM VINDO A TABUADA---------\n\n')

while numeroInformado >= 0:
    numeroInformado = int(input('INFORME UM NUMERO: '))
    print('--------------------------------------')
    if numeroInformado < 0:
        break
    for tabuada in range(11):
        print(f'{numeroInformado} x {tabuada} = {numeroInformado*tabuada}')
    print('--------------------------------------')
print('PROGRAMA ENCERRADO COM SUCESSO')
