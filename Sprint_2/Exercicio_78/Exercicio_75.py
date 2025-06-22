listaNumeros = ( int(input('Informe um numero: ')),
                int(input('Informe outro numero: ')),
                int(input('Informe mais um numero: ')) ,
                int(input('Informe outro numero: '))
)

print(f'sua lista de numeros:\n{listaNumeros}')

print(f'O numero 9 apareceu: {listaNumeros.count(9)} vezes')
print(f'O numero 3 aparece na posição {listaNumeros.index(3)}')
print('Os numeros pares são:')

for pares in listaNumeros:
    if pares % 2 == 0:
        print(pares)
