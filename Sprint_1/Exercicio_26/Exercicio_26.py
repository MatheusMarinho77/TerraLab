""" Ler uma frase e mostrar
1 - quantas vezes aparece a letra 'A'
2 - Em que posicao a letra "A" aparece a primeira vez 
3 - Em que posicao a letra "A" aparece a ultima vez 
"""

frase = str(input('Escreva uma frase que voce usa muito no seu cotidiano: '))
formataFrase = frase.lower()
quantidadeDeA = formataFrase.count('a')

print('Quantidade de vezes que a letra "A" aparece na sua frase: {}'.format(quantidadeDeA))

print('A letra "a" parece a primeria vez na posição {}'.format(formataFrase.find('a')))

print('A letra "a" parece a ultima vez na posição {}'.format(formataFrase.rfind('a')))



