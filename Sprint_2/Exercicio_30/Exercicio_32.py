## Ano bissexto  

print('Informe o ano para eu dizer se ele é bissexto ou nao')
anoInformado = int(input('Informe o ano:'))

if (anoInformado % 4 == 0 and anoInformado % 100 != 0) or anoInformado % 400 == 0 :
    print('O ano {} é bissexto'.format(anoInformado))
else:
    print('O ano {} não é bissexto'.format(anoInformado))