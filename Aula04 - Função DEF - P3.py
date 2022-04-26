# *Args **kwargs - SEP e LISTAS E DESEMPACOTAMENTOS

def func(a1, a2, a3, a4):  # Args contados
    print(a1, a2, a3, a4)
    print()

func(1, 2, 3, 4)

def func2(*args):  # Diversos Args
    # args = list[args] # Tupla ñ pode ser alterada, a linha a cima poderá, pois trans em lista
    print(args)


func2(1, 2, 3, 4)  # Retorna em tupla
Lista = [1, 2, 3, 4, 5]
Lista2 = [200, 500, 800]
print(Lista)
print(*Lista) # "*" Desempacota
print(*Lista, sep='-') # "sep=" escolhe o que vai nos espaços
print()
func2(*Lista, *Lista2)


