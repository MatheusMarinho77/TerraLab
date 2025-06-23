def cabecario():
    print('-'*30)
    print('CALCULADOR DE AREA')
    print('-'*30)


def area(largura,comprimento):
    areaTerreno = largura*comprimento
    print(f'A AREA DO SEU TERRENO DE {largura}M DE LARGURA E {comprimento}M DE COMPRIMENTO É: {areaTerreno} ')

cabecario()
lrg = float(input('Informe a Largura do terreno: '))
cmp = float(input('Informe o comprimento do terreno: '))
area(lrg,cmp)