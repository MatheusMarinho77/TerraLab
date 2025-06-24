def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError,TypeError):
            print('ERRO!! FAVOR DIGITAR UM NUMERO INTEIRO VALIDO.')
            continue
        except(KeyboardInterrupt):
            print('O USUARIO NAO DIGITOU NADA')
            return 0
        else:
            return n
        

def linha (tam = 42):
    return '-' * tam

def cabecalho(texto):
    print(linha())
    print(texto.center(40))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('SUA OPÇÃO É: ')
    return opc