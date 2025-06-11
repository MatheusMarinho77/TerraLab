import random
import math

print('BEM VINDO AO JOGO DE JOKENPÔ')
print('VAMOS COMEÇAR!!!')
jogador = int(input('Esolha:\nPEDRA = 1\nPAPEL = 2 \nTESOURA = 3\n'))
maquina = random.randint(1,3)

if (jogador == 1 and maquina == 3) or (jogador == 2 and maquina == 1) or (jogador == 3 and maquina == 2) :
    print('Voce venceu a maquina, a maquina escolheu {} '.format(maquina))
elif (jogador == 1 and maquina == 2) or (jogador == 2 and maquina == 3) or (jogador == 3 and maquina == 1):
    print('Voce perdeu, a maquina escolheu {}!!'.format(maquina))
else:
    print('O jogo ficou empatado, a maquina tambem escolheu o {}'.format(maquina))