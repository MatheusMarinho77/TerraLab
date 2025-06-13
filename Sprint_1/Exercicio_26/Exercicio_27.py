## ler o nome completo da pessoa e imformar o primeiro e ultimo nome da mesma 

nomeCompleto = str(input('Informe o nome da sua mae completo: ')).capitalize()

primeiroNome = nomeCompleto.split()
ultimoNome = primeiroNome[len(primeiroNome) - 1]

print('Primeiro nome é {}'.format(primeiroNome[0]))
print('O seu ultimo nome {}'.format(ultimoNome.capitalize()))
