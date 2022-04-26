def exibe(exibe1='', exibe2=''): print(exibe1, exibe2)

# exibe('Olá', 'Joãozinho')
# exibe('Oi', 'Maria')
# exibe('Coé', 'Cleitin')

def soma(n1=0, n2=0, n3=0): print(int(n1 + n2 + n3))

# soma(2, 1, 3)
# soma(1, 1, 1)
# soma(2, 1, 1)

def porcentomais(numero=0, porcentagem=0): print(numero / 100 * porcentagem + numero)

# porcentomais(50, 10)
# porcentomais(100, 10)
# porcentomais(10, 10)
# porcentomais(15,24)

def fizzbuzz(numero=0):
    print('fizz') if numero % 3 == 0 and not numero % 5 == 0 else numero
    print('buzz') if numero % 5 == 0 and not numero % 3 == 0 else numero
    print('fizzbuzz') if numero % 3 == 0 and numero % 5 == 0 else numero
    print(numero) if not numero % 3 == 0 and not numero % 5 == 0 else numero

fizzbuzz(10)