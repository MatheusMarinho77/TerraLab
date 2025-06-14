print('LEITOR DE PESO')
maior = -1
menor = 9999

for i in range(5):
    peso = float(input('Informe o peso atual da pessoa {} :'.format(i)))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print('Maior peso: KG {:.2f}'.format(maior))
print('Menor peso: KG {:.2f}'.format(menor))