## Programa que le o valor em metros e converte para centimetros e para milimetros 

print('Informe a altura do predio: ')
metros = float(input())

centimetros = float(metros * 100)
milimetros = float(metros * 1000)

print (' Convertendo em metros: {} m\n\n Valor em centimetros {:.3f} cm\n\n Valor em milimetros {:.3f} mm'.format(metros,centimetros,milimetros))