tabela = (
    'Flamengo',
    'Cruzeiro',
    'Bragantino',
    'Palmeiras',
    'Bahia',
    'Fluminense',
    'Atlético-MG',
    'Botafogo',
    'Mirassol',
    'Corinthians',
    'Grêmio',
    'Ceará',
    'Vasco',
    'São Paulo',
    'Santos',
    'Vitória',
    'Internacional',
    'Fortaleza',
    'Juventude',
    'Sport'
)

print('Os cinco primeiros times da tabela do Campeonato brasileiro são:\n')
for primeiros in range(0,5):
    print(tabela[primeiros])
    print()

print('OS ULTIMOS COLOCADOS DA TABELA (DO ULTIMO ATE O 16)')
for ultimos in tabela[-5:]:
    print(ultimos)
    print()

print('ORDEM ALFABETICA:')
print(sorted(tabela))
print()
    
print('EM QUE POSIÇÃO ESTA O CRUZEIRO?')
print(f'O Cruzeirão CABULOSO esta na posição{tabela.index('Cruzeiro')+1}')