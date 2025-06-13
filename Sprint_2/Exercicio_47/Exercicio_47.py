print ('Mostrador de numeros pares de 0 ate 50')
contador = int(0)

for par in range(0,51):
    if par%2 == 0:
        print(par)
        contador += 1

print('AO TODO SAO {} NUMEROS PARES NESTE INTERVALO'.format(contador))