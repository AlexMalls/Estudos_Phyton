'''
Variaveis alteradas dentro de funções não permanecem alteradas
'''

variavel = 'Valor'

def func():
    print(variavel)

def func2():
    # global variavel  # Código que altera variavel // Não recomendado
    variavel = 'Valor Editado'  #Teoricamente alteraria
    print(variavel)

func()
func2()

print(variavel)  #Porem não alterou

