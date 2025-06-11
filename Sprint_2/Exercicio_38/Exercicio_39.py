from datetime import datetime

dataAtual = datetime.now()
anoAtual = int(dataAtual.year)

print('BEM VINDO AO SITE DO EXERCITO')
print('VAMOS CONSULTAR O STATUS DO SEU ALISTAMENTO')
anoUsuario = int(input('Informe o ano do seu nascimento:'))
anoAlistamento = int(anoAtual - 18)

if anoUsuario > anoAlistamento:
    print('Ainda nao é o momento de se alistar, falta {} anos'.format(anoUsuario-anoAlistamento))
elif anoUsuario < anoAlistamento:
    print('Ja passou o tempo de se alistar em {} anos'.format(anoAlistamento - anoUsuario))
else:
    print('OPA, ESTA NO ANO DE SE ALISTAR!!! voce completou 18 anos.')