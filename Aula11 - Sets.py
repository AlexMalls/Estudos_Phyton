# Add (adiciona), update (atualiza), clear, discard
# Union (une)
# Insertion & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

set1 = {1, 2, 'Alexandre', 4, 5}
set1.add('José')
set1.add(2) # Se já possui ela não adiciona
set1.add(3) # Set não respeitam ordem, aperte F10 varias vezes e veja

print(set1)
print()


lista = [1,2,5,3,3,1,1,5,5,4,2,2,2,4,5,6,8,7,'Alex','Alex','Alex'] #Elementos duplicados
print(lista)
lista = set(lista) # Transformando em set ele remove as duplicatas
lista = list(lista)
print(lista)
print()
print('------------------------------------------------------------')
print()

s1 = {1,2,3, 4, 'alex'}
s2 = {3,4,5,6}
s3 = s1 | s2
s4 = s1 & s2
s5 = s1 - s2
s6 = s1 ^ s2

print(s3)
print(s4)
print(s5)
print(s6)