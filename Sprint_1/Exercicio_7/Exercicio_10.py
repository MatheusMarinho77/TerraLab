##CONVERTER REAIS EM DOLLAR

reais = float(input('Informe o valor que voce possui no seu banco: '))
usd = float(reais/5.59)

print('O valor que voce possui R${:.2f} da para comprar atualmente U${:.2f}'.format(reais,usd))