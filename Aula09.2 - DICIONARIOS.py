'''
Fazendo um sistema de Clientes
'''
Ncliente = 0
Cliente = ''
Clientes = {}
exit = False

def Novo_Cliente():
    Nome = input('Qual o nome do cliente? ')
    Sobrenome = input('Qual o sobrenome do cliente? ')
    return Nome, Sobrenome

while not exit:
    print('Bem vindo ao sistema de cliente')
    print('Digite 1 para VERIFICAR clientes cadastrados')
    print('Digite 2 para CADASTRAR novos clientes')
    Trigger = input('O que você deseja fazer? ')
    if Trigger == '1':
        for C, N in Clientes.items():
            print(C, N)


    if Trigger == '2':
        Ncliente = Ncliente+1
        Clientes['Cliente'+str(Ncliente)] = Novo_Cliente()
        print(Clientes)
