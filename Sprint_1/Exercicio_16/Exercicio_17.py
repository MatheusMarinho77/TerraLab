## Calculo da Hipotenusa de um triangulo

import math

print('Ola, favor informar o comprimento do cateto oposto e do cateto adjacente')

catOposto = float(input('Cateto oposto: '))
catAdjacente = float(input('Cateto Adjacente: '))
hipotenusa = float(math.pow(catAdjacente,2) + math.pow(catOposto,2))

print('A hipotenusa do triangulo retangulo é {:.2f}'.format(math.sqrt(hipotenusa)))


