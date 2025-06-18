item = 'n'
preco = 0 
totalGasto = 0
maisDe1000 = 0
maisBarato = 9000000000000000000000
nomeMaisBarato = 'a'
continuar = True

while continuar != False:
    print('CADASTRO DOS PRODUTOS\n')
    item = str(input('Informe o nome do produto: \n')).capitalize()
    preco = float(input('Informe seu preço: R$'))
    totalGasto = totalGasto + preco
    if preco >= 1000:
        maisDe1000 += 1
    if preco <= maisBarato:
        maisBarato = preco
        nomeMaisBarato = item 
    continuar = str(input('DESEJA CONTINUAR? [S/N]')).upper() 
    if continuar == 'N':
        break

print(f'TOTAL GASTO R${totalGasto}')
print(f'PRODUTOS MAIS CARO QUE R$1.000 : {maisDe1000}')
print(f'NOME DO PRODUTO MAIS BARATO: {nomeMaisBarato.capitalize()}')
