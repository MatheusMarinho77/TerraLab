# Ler dois numeros inteiros e compara-los

print('Bem vindo ao comparador de valores\nPreciso que digite o valor de dois numeros inteiro!!!')
numero1 = int(input('PRIMEIRO NUMERO:'))
numero2 = int(input('SEGUNDO NUMERO:'))

if numero1 > numero2:
    print('O primeiro numero informado ou seja com valor de {} é maior que o segundo numero que possui o valor de {}'.format(numero1,numero2))
elif numero2 > numero1:
    print('O segundo numero informado ou seja com valor de {} é maior que o primeiro numero que possui o valor de {}'.format(numero2,numero1))
else:
    print('Os numero informados possuem o mesmo valor o seja, são iguais')
