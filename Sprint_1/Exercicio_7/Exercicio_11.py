#Quantidade de tintas para se limpar uma 

largura = float(input('Informe a largura da parede:'))
altura = float(input('Informe a altura da parede:'))

area = float(largura * altura)
tinta = float(area/2)

print('A AREA A SER PINTADA É DE {:.2f}m E É NESCESSARIO {:.2f} LITROS DE TINTAR PARA PINTAR A PAREDE'.format(area,tinta))