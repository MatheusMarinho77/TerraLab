import random

numeroSorteado = random.randint(0,10)
numeroInformado = -50
tentativas = 1

while numeroInformado != numeroSorteado:
    numeroInformado = int(input('Tente adivinhar o numero sorteado entre 0 a 10:'))
    if numeroInformado != numeroSorteado:
        print('Nao é o numero {}\nTente novamente.'.format(numeroInformado))
        tentativas +=1
print('Parabens voce conseguiu, o numero escolhido era o {}'.format(numeroSorteado))
print('numero de tentativas {}'.format(tentativas))

