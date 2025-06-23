import moeda

valorInformado = float(input('Informe o valor que deseseja calcular: R$'))
print(f'Com o aumento do preço em R$50,00 o valor vai para R${moeda.aumentar(valorInformado)}')
print(f'Com o desconto de R$50,00 o valor vai para R${moeda.diminuir(valorInformado)}')
print(f'O valor R${valorInformado} foi dobrado, logo foi para R${moeda.dobro(valorInformado)}')
print(f'A metade do valor é R${moeda.metade(valorInformado)}')

