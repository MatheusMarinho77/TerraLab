import math
import random

listaNumeros = (random.randint(0,20), random.randint(0,20), random.randint(0,20), random.randint(0,20),random.randint(0,20))

menorNumero = 999
for c in range(len(listaNumeros)):
    if listaNumeros[c] <= menorNumero:
        menorNumero = listaNumeros[c]

maiorNumero = -999
for c in range(len(listaNumeros)):
    if listaNumeros[c] >= maiorNumero:
        maiorNumero = listaNumeros[c]

print(f' A lista dos numeros gerados é:\n{listaNumeros}')
print(f'O menor numero da lista é {menorNumero}')
print(f'O maior numero da lista é {maiorNumero}')



