listaPalavras = ('Palavra', 'Casa', 'Cachorro', 'Bebida', 'Raçao')

for p in listaPalavras:
    print(f'\nA palavra {p} possui as silabas: ', end='')
    print()
    for silabas in p:
        if silabas.lower() in 'aeiou':
            print(silabas, end=' ')
