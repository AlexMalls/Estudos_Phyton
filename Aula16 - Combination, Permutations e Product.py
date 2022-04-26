"""
Combinação - Ordem não importa
Permutação - Ordem importa
             ambos não repetem valors únicos
Produtos   - Ordem importa e repete valores únicos
"""
import itertools

Contador1 = itertools.count()
Contador2 = itertools.count()
Contador3 = itertools.count()
Clientes = ['Alexandre', 'Fernanda', 'Luiz', 'Vinicius', 'Guilherme']

for grupo in itertools.combinations(Clientes, 2):
    print(next(Contador1), grupo)
print('-'*50)

for grupo in itertools.permutations(Clientes, 2):
    print(next(Contador2), grupo)
print('-'*50)

for grupo in itertools.product(Clientes, repeat=2):
    print(next(Contador3), grupo)
print('-'*50)