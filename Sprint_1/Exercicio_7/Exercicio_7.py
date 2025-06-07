## Programa que calcula a media de duas notas do aluno

print('Ola aluno, favor informar ao sistemas suas notas:')

nota1 = float(input('Informe quanto tirou na primeira prova: '))
nota2 = float(input('Agora informe quanto tirou na segunda avaliação: '))
mediaNotas = float((nota1 + nota2) / 2)

print ('Sua media nas provas é igual a {:.3f}'. format(mediaNotas))