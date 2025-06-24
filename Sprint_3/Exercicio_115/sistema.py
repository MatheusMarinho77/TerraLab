from lib.interface import *
from lib.arquivo import *
from time import sleep

arquivo = 'cadastro.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['VER PESSOAS CADASTRADAS','CADASTRAR NOVA PESSOA','SAIR DO SISTEMA'])
    if resposta == 1:
        cabecalho('OPÇÃO 1')
        lerArquivo(arquivo)
        sleep(1)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome:'))
        idade = leiaInt('Idade:')
        cadastrar(arquivo, nome, idade)
        sleep(1)
    elif resposta == 3:
        cabecalho('PROGRAMA ENCERRADO COM SUCESSO')
        break
    else:
        cabecalho('ERRO CIRITICO!!! OPÇÃO INVALIDA, DIGITE UMA OPÇÃO VALIDA')
        sleep(1)
    