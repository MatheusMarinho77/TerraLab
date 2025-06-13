somador = int(0)

for numero in range(1,500):
    if numero % 2 != 0:
        if numero % 3 == 0:
            print(numero)
            somador += numero

print('A SOMA FINAL DOS NUMEROS IMPARES MULTIPLOS DE 3 É IGUAL A: {}'.format(somador))