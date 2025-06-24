from lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close
    except:
        print('HOUVE UM ERRO NA CRIAÇÃO DO ARQUIVO')
    else:
        print(F'ARQUIVO {nome} CRIADO COM SUCESSO')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO AO LER O ARQUIVO')
    else:
        cabecalho('PESSOAS CADASTRADAS COM SUCESSO')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}, {dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arquivo , nome = 'desconhecido' , idade = 0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Houve um erro ao tentar cadastrar a pessoa')
    else:
        try:    
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao tentar escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()