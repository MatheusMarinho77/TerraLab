print('------BEM VINDO AO SISTEMA BANCARIO------')
valorCasa = float(input('informe o valor da casa que deseja comprar:'))
print()
salarioComprador = float(input('Informe seu salario R$'))
print()
tempoParaPagar = int(input('Informe em quantos anos deseja quitar a casa:'))*12
print('\n')


valorPrestaçao = float(valorCasa/tempoParaPagar)
maxPrestação = float((salarioComprador*0.3) * tempoParaPagar)

if maxPrestação < valorCasa:
    print('Emprestimo negado.\nO valor pago ao final do tempo de financiamento nao sera suficente.')
    print('Valor da casa: R${:.2f}'.format(valorCasa))
    print('Valor MAXIMO que pode ser pago ao final do emprestimo de {} anos: R${:.2f}'.format(int(tempoParaPagar/12),maxPrestação))
else:
    print('O financiamento pode ser realizado nesses moldes.')
    print('Valor do imovel: R${:.2f}\nValor da sua prestação: R${:.2f}'.format(valorCasa,valorPrestaçao))


