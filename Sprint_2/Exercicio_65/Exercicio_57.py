sexo = str(input('Digite seu sexo [M/F]')).upper()
while sexo not in 'MF':
    sexo = str(input('Digite seu sexo corretamente')).upper()
print('Obrigado por informar seu sexo.')