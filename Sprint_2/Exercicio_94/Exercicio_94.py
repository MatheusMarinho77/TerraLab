dicio = {}
pessoas = []
mediaIdade = 0

while True:
    dicio['Nome'] = str(input('\nNome: ')).strip().title()
    dicio['Idade'] = int(input('Idade:'))
    dicio['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]

    while dicio['Sexo'] != 'M' and dicio['Sexo'] != 'F':
        dicio['Sexo'] = str(input('Decisão inválida! Sexo: [M/F]')).upper()[0]
    pessoas.append(dicio.copy())

    decisão = str(input('Deseja continuar o cadastro? [S/N] ')).upper()[0]

    while decisão != 'S' and decisão != 'N':
        decisão = str(input('Decisão inválida! Deseja continuar o cadastro? [S/N] ')).upper()[0]

    if decisão == 'N':
        break

for p in pessoas:
    mediaIdade += p['Idade']

if len(pessoas) > 0:
    media_final = mediaIdade / len(pessoas)
else:
    media_final = 0

print(f'\nTotal de pessoas cadastradas foram {len(pessoas)}.')
print(f'Média das idades é {media_final:.2f}.')

print('As mulheres cadastradas foram ', end='')
for p in pessoas:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]}', end=' ')

print('\nLista de pessoas com idade acima da média:')
for p in pessoas:
    if p['Idade'] >= media_final:
        print(f'   Nome: {p["Nome"]}, Idade: {p["Idade"]}, Sexo: {p["Sexo"]}')
print()