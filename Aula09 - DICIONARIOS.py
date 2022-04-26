'''
 Dicionario é como uma lista entretanto com
 indices não pré estabelecidos pelo phyton
'''

Dicio1 = {'chave1':'valor da chave'}
Dicio1['chave2'] = 'Valor da chave2'

print(Dicio1)
print(Dicio1['chave2'])
print()

Dicio2 = dict(chave1='valor chave1', chave2='valor chave2')
Dicio2['chave3'] = 'Valor da 3'

print(Dicio2)
print(Dicio2.get('chave3')) # .get evita o ERRO caso não exista
print(Dicio2.get('chave4')) if 'chave4' in Dicio2 else None # IF NOT evita retornar NONE
print()

print('chave3' in Dicio1)
print('chave3' in Dicio2)