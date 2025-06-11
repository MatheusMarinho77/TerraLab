import datetime

anoAtual = datetime.datetime.today()
anoAtual = anoAtual.year
anoNascimento = int(input('OLA ATLETA, INFORME O ANO DE NASCIMENTO SEU:'))
idade = int(anoAtual - anoNascimento)

if idade < 9:
    print('SUA CATEGORIA: MIRIM')
elif idade >= 9 and idade < 14:
    print('SUA CATEGORIA: INFANTIL')
elif idade >= 14 and idade < 19:
    print('SUA CATEGORIA: JUNIOR')
elif idade >= 19 and idade < 20:
    print('SUA CATEGORIA: SENIOR')
else:
    print('SUA CATEGORIA É MASTER')