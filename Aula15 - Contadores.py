"""
Count - Itertools
"""

from itertools import count

contador = count()
contador2 = count(start=5)
contador3 = count(start=2, step=2)
contador4 = count(step=0.1)
contador5 = count(start=-1, step=-1)

for valor in contador:
    print(valor) #Cuidado pra não fazer isto pois gerará um looping infinito
    if valor >= 10: break # Evita o looping infinito
print('-'*20)

for valor in contador2:
    print(valor)
    if valor >= 10: break # Evita o looping infinito
print('-'*20)

for valor in contador3:
    print(valor)
    if valor >= 10: break # Evita o looping infinito
print('-'*20)

for valor in contador4:
    print(round(valor,2))
    if valor >= 1: break # Evita o looping infinito
print('-'*20)

for valor in contador5:
    print(round(valor,2))
    if valor >= 1 or valor <= -10: break # Evita o looping infinito
print('-'*20)

'------------------------------------------------------------------------'
'Uso disto: Colocar indices em elementos'

lista = ['Alexandre', 'Fernanda', 'Vinicius', 'Guilherme']

lista = zip(contador, lista)
lista = list(lista)
print(lista)
