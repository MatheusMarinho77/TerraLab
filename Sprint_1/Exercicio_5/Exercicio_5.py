# Programa que le um numero inteiro e mostra seu sucessor e seu antecessor

print('Ola usuario, informe um numero inteiro: ')

numero = int(input())
antecessorNum = int(numero - 1)
sucessorNumero = int(numero + 1)

print('O numero informado {:^5}\npossui como antecessor o numero {:^5}\ncomo sucessor o {:^5}.'.format(numero,antecessorNum,sucessorNumero))

