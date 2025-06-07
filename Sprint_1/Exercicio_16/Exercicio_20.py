##sjefoesnfois

from random import shuffle

listaDosCanditados = []

nome1 = str(input('Primeiro candidato:'))
nome2 = str(input('Segundo candidato:'))
nome3 = str(input('Terceiro candidato:'))
nome4 = str(input('Quarto candidato:'))

listaDosCanditados = [nome1,nome2,nome3,nome4]
shuffle(listaDosCanditados)

print('A ordem de apresentação sera: 1- {}\n2- {}\n3- {}\n4- {} '.format(listaDosCanditados[0],listaDosCanditados[1],listaDosCanditados[2],listaDosCanditados[3]))

