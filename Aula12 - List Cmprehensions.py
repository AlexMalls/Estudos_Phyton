
l1 = [1, 2, 3, 4, 5]
l2 = [Index for Index in l1]
l3 = [Index * 2 for Index in l1]
l4 = [(Index, Index2) for Index in l1 for Index2 in range(3)]

print(l2)
print(l3)
print(l4)

print()
print('---------------------------------------------------')
print()

lst1 = ['alex', 'fernanda', 'luiz']
lst2 = [Index.replace('a', '@').upper() for Index in lst1]

print(lst2)

print()
print('---------------------------------------------------')
print()

Tupla = (
    ('Chave1', 'Valor1'),
    ('Chave2', 'Valor2'),
)
Tupla2 = [(V, C) for C, V in Tupla]

print(Tupla)
print(Tupla2)

print()
print('---------------------------------------------------')
print()

L1 = list(range(16))
L2 = [I for I in L1 if I % 2 == 0]
L3 = [I for I in L1 if I % 2 == 0 if I % 3 == 0]

print(L1)
print(L2)
print(L3)