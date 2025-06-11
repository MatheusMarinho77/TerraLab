
print('Informe o tamanho de 3 retas: ')

reta1 = float(input('Comprimento da reta 1: '))
reta2 = float(input('Comprimento da reta 2: '))
reta3 = float(input('Comprimento da reta 3: '))

if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    print('É possível formar um triângulo com essas 3 retas!')

    if reta1 == reta2 and reta1 == reta3:
        print('O triângulo é EQUILÁTERO (todos os lados iguais).')
    elif (reta1 == reta2) or (reta1 == reta3) or (reta2 == reta3):
        print('O triângulo é ISÓSCELES (possui 2 lados iguais).')
    else:
        print('O triângulo é ESCALENO (todos os lados diferentes).')
else:
    print('NÃO é possível formar um triângulo com essas 3 retas.')