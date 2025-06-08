## verificar se o nome da cidade começa com SANTO

cidade = str(input('Informe o nome de uma cidade: '))

verificação = cidade.split()
primeiraLetra = verificação[0].capitalize()

print('A cidade começa com o nome "Santo" ?')
print('Santo' in primeiraLetra)
