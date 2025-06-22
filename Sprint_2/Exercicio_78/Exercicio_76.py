tabelaPreço = ( 'Pão' , 0.70,
                'Presunto', 6.50,
                'Mussarela', 7.50,
                'Cafe', 3.00
)

print('\nTabela Preço\n')
item = str('ITEM')
preco = str('PREÇO')

print(f'{item:.<30}', end='')
print(f'{preco:<30}')

for pos in range(len(tabelaPreço)):
    if pos % 2 == 0:
        print(f'{tabelaPreço[pos]:.<30}', end='')
    else:
        print(f'R${tabelaPreço[pos]:.2f}')