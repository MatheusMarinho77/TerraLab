""" Programa que le nome completo e:
1 - todas as letras maiusculas  
2 - todas as letras minusculas 
3 - Quantas letras tem (sem contar os espaços)
4- quantas letras tem o primeiro nome
"""

nome = str(input('Informe seu nome completo:'))

print('Nome com todas as letras maiusculas: {}'.format(nome.upper()))
print('Nome com todas as letras minusculas: {}'.format(nome.lower()))

letraMinuscula = str(nome.replace(' ',''))
print('Quantas letras tem o seu nome {}: {}'.format(letraMinuscula,len(letraMinuscula)))

primeiroNome = nome.split()
print('O primeiro nome possui {} letras'.format(len(primeiroNome[0])))

