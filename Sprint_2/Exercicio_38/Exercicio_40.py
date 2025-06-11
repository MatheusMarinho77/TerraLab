print('Sistemas de calculo de media das notas')

nota1 = float(input('Informe sua primeira nota:'))
nota2 = float(input('Informe sua segunda nota:'))
media = float((nota1 + nota2)/2)

if media < 5.0:
    print('REPROVADO!!! Sua media foi de {:.2f} '.format(media))
elif media >= 5.0 and media < 7.0:
    print ('VOCE ESTA DE RECUPERAÇÃO!!! sua media no foi de {:.2f}'.format(media))
else:
    print('PARABENS VOCE FOI APROVADO!!! SUA MEDIA FOI DE {:.2f}'.format(media))

