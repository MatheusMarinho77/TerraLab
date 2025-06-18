import random

numeroJogador = 0
numeroComputador = 0
perdeu = False
contadorVitorias = 0

print('----------BEM VINDO AO GAME E PAR OU IMPAR----------')
print()

while perdeu != True:
    escolhaJogador = str(input('ESCOLHA PAR OU IMPAR:\n')).upper()
    if escolhaJogador == 'PAR':
        escolhaComputador = 'IMPAR'
        numeroJogador = int(input('ESCOLHA UM NUMERO: '))
        numeroComputador = random.randint(0,10)
        resultado = numeroComputador + numeroJogador
        if resultado % 2 == 0:
            print(f'VOCE VENCEU!!!{numeroJogador} + {numeroComputador} é PAR')
            contadorVitorias += 1
        else :
            print(f'VOCE PERDEU PARA O COMPUTADOR!!!{numeroJogador} + {numeroComputador} é IMPAR')
            perdeu = True
            break
    elif escolhaJogador == 'IMPAR':
        escolhaComputador = 'PAR'
        print('-----------------------------------------------------------')
        numeroJogador = int(input('ESCOLHA UM NUMERO: '))
        numeroComputador = random.randint(0,10)
        resultado = numeroComputador + numeroJogador
        if resultado % 2 != 0:
            print('-----------------------------------------------------------')
            print(f'VOCE VENCEU!!!{numeroJogador} + {numeroComputador} é IMPAR')
            contadorVitorias += 1
        else :
            print('-----------------------------------------------------------')
            print(f'VOCE PERDEU!!!{numeroJogador} + {numeroComputador} é PAR')
            perdeu = True
            break

    else :   
        print('ESCOLHA INVALIDA')


print(f'VOCE TEVE O TOTAL DE {contadorVitorias} VITORIAS CONSECUTIVAS')

                
