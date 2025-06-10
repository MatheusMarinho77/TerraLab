## eu tentar acertar o numero sorteado entre 0 a 5 que o computador 

import random
import math

numeroAlaetorio = int(random.randrange(0, 6))

print('Bem vindo ao jogo de adivinhação!')
numeroUsuario = int(input('Escolha um numero entre 0 e 5: '))

if numeroUsuario == numeroAlaetorio:
    print('Numero sorteado pelo computador: {}'.format(numeroAlaetorio))
    print('Parabens, voce adivinhou o numero sorteado pelo computador.')
else:
    print('Que pena, voce escolheu o numero errado, o numero que voce escolheu é o {}, mas o numero correto seria {}'.format(numeroUsuario,numeroAlaetorio))
print('Programa encerrado, obrigado por participar.')