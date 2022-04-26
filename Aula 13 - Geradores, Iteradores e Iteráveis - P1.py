import sys

lista  = [0,1,2,'alex',5]
print(hasattr(lista,'__next__'))

lista = iter(lista)
print(hasattr(lista,'__next__'))

print()

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))


print('------------------------------------------------------------------------')

L1 = [x for x in range(10000000)]
print(sys.getsizeof(L1))
L2 = (x for x in range(10000000))
print(sys.getsizeof(L2))




