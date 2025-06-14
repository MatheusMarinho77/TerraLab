from datetime import datetime

ano = datetime.today().year
maiorDeIdade = 0
menorDeIdade = 0

for i in range(7):
    dataNascimento = int(input('Informe o ano do seu nascimento: '))
    idade = ano - dataNascimento
    if idade >= 18:
        maiorDeIdade += 1
    elif idade < 18:
        menorDeIdade += 1

print('QUANTIDADE DE PESSOAS MAIORES DE IDADE: {}\n'.format(maiorDeIdade))
print('QUANTIDADE DE PESSOAS MENORES DE IDADE: {}\n'.format(menorDeIdade))