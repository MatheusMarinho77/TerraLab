print('Informe o valor do seu produto:')
valor = float(input('Valor do produto: '))
print('INFORME A FORMA DE PAGAMENTO PELO SEU NUMERO INICIAL :')
tipoPagamento = int(input('1 - A VISTA NO DINHEIRO/CHEQUE\n2 - A VISTA CARTÃO\n3 - EM ATE 2X NO CARTÃO\n4 - 3X OU MAIS NO CARTÃO\n'))
print()

if tipoPagamento == 1:
    valorFinal = valor - (valor * 0.10)
    print('Voce obteve 10% de desconto devido a forma de pagamento, o valor final é R${:.2f}'.format(valorFinal))
elif tipoPagamento == 2:
    valorFinal = valor - (valor * 0.05)
    print('Voce obteve 5% de desconto devido a forma de pagamento, o valor final é R${:.2f}'.format(valorFinal))
elif tipoPagamento == 3:
    valorFinal = valor
    print('O valor final é R${:.2f}'.format(valorFinal))
elif tipoPagamento == 4:
    valorFinal = valor * 1.2
    print('Pela forma de pagamento o preço do produto passou de R${:.2f} para R${:.2f}'.format(valor,valorFinal))