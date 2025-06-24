import moeda


valorInformado = float(input('Informe o valor que deseseja calcular: R$'))
print(f'{moeda.moeda(valorInformado,True)} + 50 é = {moeda.aumentar(valorInformado, True)}')
print(f'Com o desconto de R$50,00 o valor vai para {moeda.diminuir(valorInformado,True)}')
print(f'O valor {moeda.moeda(valorInformado,False)} foi dobrado, logo foi para {moeda.dobro(valorInformado, False)}')
print(f'A metade do valor é {moeda.metade(valorInformado,True)}')

