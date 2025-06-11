## Ler 3 retas e dizer se podem formar um triangulo

import math

print('Informe para o tamanho de 3 retas: ')

reta1 = float(input('Comprimento da reta 1:'))
reta2 = float(input('Comprimento da reta 2:'))
reta3 = float(input('Comprimento da reta 3:'))

if (reta1 + reta2 <= reta3) or (reta1 + reta3 <= reta2) or (reta2 + reta3 <= reta1):
    print('Nao é possivel formar um triangulo com essas 3 retas !!!')
else :
    print('É possivel fazer um triangulo com essas retas.')
