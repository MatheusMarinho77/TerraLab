#ler de 0 ate 9999 e mostra cada casa

numero = int(input('Informe um numero de 0 ate 9999: '))

unidade = int((numero/1) % 10)
dezena = int((numero/10) % 10)
centena = int((numero/100) % 10)
miliar = int((numero/1000) % 10)

print('unidade: {}'.format(unidade))
print('dezena: {}'.format(dezena))
print('dentena: {}'.format(centena))
print('miliar: {}'.format(miliar))
