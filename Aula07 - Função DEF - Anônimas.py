"""
Expressões Lambda ou Anônimas
"""

def multi(arg, arg2):
    return arg * arg2
print(multi(2,2))


a = lambda x, y: x * y
print(a(2,2))
print()
print('-----------------------------------------')
print()

#Aplicação PRATICA (Lista de produtos (Ordenação))

lista = [
    ['Produto6', 15],
    ['Produto2', 25],
    ['Produto4', 52],
    ['Produto3', 18],
    ['Produto5', 6],
    ['Produto1', 8.5]
]
#lista.sort(key=lambda item: item[0]) # Altera a ordem da lista
print(sorted(lista, key=lambda item: item[1])) # Não altera a lista só demonstra ordenado
print(lista)


