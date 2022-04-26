Produtos = []

Produtos.append(('Produto_1', 25))
Produtos.append(('Produto_2', 35))
Produtos.append(('Produto_3', 30))
Produtos.append(('Produto_4', 10))

Soma = sum([float(x[1]) for x in Produtos])

print(Soma)