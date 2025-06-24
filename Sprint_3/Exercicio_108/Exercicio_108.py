import moeda

valorInformado = float(input('Informe o valor que deseseja calcular: R$'))
print(f'Com o aumento do preço em R$50,00 o valor vai sai de {moeda.moeda(valorInformado)} para {moeda.moeda(moeda.aumentar(valorInformado))}')
print(f'Com o desconto de R$50,00 o valor vai para {moeda.moeda(moeda.diminuir(valorInformado))}')
print(f'O valor {moeda.moeda(valorInformado)} foi dobrado, logo foi para {moeda.moeda(moeda.dobro(valorInformado))}')
print(f'A metade do valor é {moeda.moeda(moeda.metade(valorInformado))}')

