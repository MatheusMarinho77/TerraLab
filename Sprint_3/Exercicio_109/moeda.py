def aumentar(valor, formatar = False):
    resultado = valor + 50
    if formatar == False:
        return resultado
    else:
        return moeda(resultado)

def diminuir(valor, formatar = False):
    resultado = valor - 50
    if formatar == False:
        return resultado
    else:
        return moeda(resultado)

def dobro(valor, formatar = False):
    resultado = valor * 2
    if formatar == False:
        return resultado
    else:
        return moeda(resultado)

def metade (valor, formatar = False):
    resultado = valor/2
    if formatar == False:
        return resultado
    else:
        return moeda(resultado)

def moeda(valor, formatar = False):
    if formatar == True:
        return f'R${valor:.2f}'.replace('.',',')
    else:
        return f'R${valor:.2f}'