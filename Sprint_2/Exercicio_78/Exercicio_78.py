listaNumerica = list()
qntdNumeros = 5
maior = 0
menor = 0
posicaoMaior = 0
posicaoMenor = 0

for i in range(qntdNumeros):
    numeroInformado = int(input('Informe um valor para ser adicionada na lista:\n'))
    listaNumerica.append(numeroInformado)
    if i == 0:
        maior = numeroInformado
        menor = numeroInformado
        posicaoMaior = i
        posicaoMenor = i

    else:
        if numeroInformado > maior:
            maior = numeroInformado
            posicaoMaior = i
        elif numeroInformado < menor:
            menor = numeroInformado
            posicaoMenor = i

print(f'menor numero digitado é o {menor}, e sua posição é a {posicaoMenor}')
print(f'maior numero digitado é o {maior}, e sua posição é a {posicaoMaior}')
