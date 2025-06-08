##Pessoa possui Silva no nome?

nome = str(input('Informe seu nome completo:'))
nomeSeparado = nome.upper().split()

print('O nome possui "Silva no sobrenome? \n ')
print('SILVA' in nomeSeparado)