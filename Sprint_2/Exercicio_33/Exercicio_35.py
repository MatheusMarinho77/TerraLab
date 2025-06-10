## Ler 3 retas e dizer se podem formar um triangulo

import math

print('Informe para o tamanho de 3 retas: ')

reta1 = float(input('Comprimento da reta 1:'))
reta2 = float(input('Comprimento da reta 2:'))
reta3 = float(input('Comprimento da reta 3:'))

if math.ceil(reta1,2) + math.ceil(reta2,2) < math.ceil(reta3,2):
math.