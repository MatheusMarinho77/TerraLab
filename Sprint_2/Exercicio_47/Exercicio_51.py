## Progressão aritmetica 

somador = int(0)

print('PROGRAMA DE PROGRESSÃO ARITIMETICA')

termoInicial = int(input('TERMO INICIAL DA PA: '))
razao = int(input('QUAL A RAZAO DA SUA PA?'))

decimoTermo = termoInicial + ((10 - 1)*razao)

for contador in range(termoInicial,decimoTermo + 1,razao):
    print(contador)
