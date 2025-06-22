listaNumeros = []

for i in range(6):
    numeroInformado = int(input('informe um numero para adicionarmos a lista: '))
    if i == 0:
        listaNumeros.append(numeroInformado)
    else:
        if numeroInformado in listaNumeros:
            continue
        else:
            listaNumeros.append(numeroInformado)

print(sorted(listaNumeros))