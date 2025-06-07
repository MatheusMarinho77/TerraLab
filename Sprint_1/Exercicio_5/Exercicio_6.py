# PROGRAMA QUE LE UM NUMERO E MOSTRA SEU DOBRO, O TRIPLO E SUA RAIZ QUADRADA

print('Informe um numero para o programa:')
numero = int(input())

dobroNum = numero * 2
triploNum = numero * 3
raizNum = float(numero ** (1/2))

print('O numero {}, multiplicado por 2 é igual a {}'.format(numero,dobroNum))
print('O numero {}, multiplicado por 3 é igual a {}'.format(numero,triploNum))
print('A raiz quadrada do numero {}, é igual a {:.3f}'.format(numero,raizNum))