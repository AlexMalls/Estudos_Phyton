"""
Função DEF parte 1
"""
def funcao():
    print('Hello shit')
    print('Hello my honey')

funcao()
funcao()

"""
Parametros da função
"""

def Print(msg1='Sem mensagem', msg2='Sem Mensagem 2'):
    msg1 = msg1.replace('a', '4')
    msg2 = msg2.replace('e', '3')

    print(msg1)
    print(msg2)

print('--------------------------')
print()
# Print() #ERRO Pois o parametro não está definido como msg1 e msg2
Print('Mensagem', 'Feita')
Print('Feita', 'Mensagem')
print()

Print()
print()

Print('Mensagem')
print()

Print(msg2='Mensagem')
print('--------------------------')


