"""
Função DEF parte 2  ------ RETURN E MAIS EXEMPLOS
"""
def func(var):
    print(var)
    return var # RETURN é o que atribuirá 'VAR' na função logo ela será preenchida e retornará TRUE
    # print('Isto não será executado pois está depois do RETURN')

Variavel = func(input('Digite algo: '))
print(f'O valor retornado da variavel "Variavel" é: {Variavel}')

if Variavel: #if Variavel = TRUE:
    print()
    print('Variavel TRUE')
else:
    print()
    print('Variavel False')

print('-------------------------------')

def divisao(n1, n2):
    if int(n2) > 0:
        result = int(n1) / int(n2)
        return result
    return n1

try: resultado = divisao(input('Digite o 1º numero: '), input('Digite o 2º numero: '))
except: resultado = 'Deve conter apenas numeros'

print(resultado) if resultado else print(resultado)