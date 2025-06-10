"""Programa de multa
1 - ler a velocidade do carro 
2 - se ele ultrapassar 80km, entao multa-lo
3 - cada km excedido vai custar R$7,00
"""

velocidadeCarro = int(input('Informe a velocidade do carro ao passar no radar: '))

if velocidadeCarro >= 80:
    print('MULTADOR !!! O carro estava acima do limite de velocidade.')
    valorMulta = float(7.00*(velocidadeCarro - 80))
    print('Valor da multa que tem que ser paga: R${:.2f}'.format(valorMulta))
else :
    print('O carro estava dentro do limite de velocidade!!!')
print('PROGRAMA ENCERRADO')