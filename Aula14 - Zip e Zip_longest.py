from itertools import zip_longest, count

Indice = count()
Cidades = ['São Paulo', 'Porto Alegre', 'Rio de Janeiro', 'Salvador']
Estados = ['SP', 'RS', 'RJ']


CidadesEstados = zip(Indice, Estados, Cidades)
print(list  (CidadesEstados))

# CidadesEstados = zip_longest(Indice, Estados, Cidades)
# print(list  (CidadesEstados))

# CidadesEstados = zip_longest(Indice, Estados, Cidades, fillvalue='Estado')
# print(list  (CidadesEstados))
