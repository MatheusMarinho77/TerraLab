numeros = ('Zero', 'Um', 'Dois','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezesete','Dezoito','Dezenove','Vinte')

n = int(input('Digite um numero entre 0 e 20:'))
if n > 20 and n < 0:
    n = int(input('ERRO, TENTE NOVAMENTE!! \nDigite um numero entre 0 e 20:'))
print (f'Voce digitou o numero {numeros[n]}')