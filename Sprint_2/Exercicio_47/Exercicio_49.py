##Tabuada de um numero

numeroInformado = int(input('Informe um numero:'))
print('TABUADA DO NUMERO {}\n'.format(numeroInformado))

for tabuada in range(0,11):
    resultado = int(numeroInformado*tabuada)
    print('{} x {} = {}'.format(numeroInformado,tabuada,resultado))

print('TABUADA FINALIZADA COM SUCESSO')