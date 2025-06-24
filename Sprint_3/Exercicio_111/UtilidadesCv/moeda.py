def calculador (valor, aumento, reducao):
    valorFormatado = f'R${valor:.2f}'.replace('.',',')

    dobro = float(valor * 2)
    dobroFormat = f'R${dobro:.2f}'.replace('.',',')

    metade = float(valor / 2)
    metadeFormat = f'R${metade:.2f}'.replace('.',',')

    imprimirAumento = aumento
    aumento = float(valor * (1 + (aumento/100)))
    aumentoFormat = f'R${aumento:.2f}'.replace('.',',')
    
    imprimirReducao = reducao
    reducao = float(valor * (1 - (reducao/100)))
    reducaoFormat = f'R${reducao:.2f}'.replace('.',',')

    print('-'*30)
    print('CALCULADORA TERRALAB')
    print('-'*30)
    print(f'Valor informado {valorFormatado}')
    print(f'Seu dobro é igual a {dobroFormat}')
    print(f'Ja sua metade é igual a {metadeFormat}')
    print(f'Aumentando {imprimirAumento}% o valor vai para {aumentoFormat}')
    print(f'Reduzindo {imprimirReducao}% o valor vai para {reducaoFormat}')
