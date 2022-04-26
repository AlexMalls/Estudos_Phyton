from itertools import groupby, tee
#  Para que o Groupby funcione, o agrupamento deve estar por odem
#  No exemplo a baixo o agrupamento será feito por NOTA

alunos = [
    {'Nome': 'Alexandre', 'Nota': 'A'},
    {'Nome': 'Fernanda', 'Nota': 'B'},
    {'Nome': 'Luiz', 'Nota': 'D'},
    {'Nome': 'Guilherme', 'Nota': 'A'},
    {'Nome': 'Vinicius', 'Nota': 'B'},
    {'Nome': 'Alisonete', 'Nota': 'C'},
    {'Nome': 'Bruno', 'Nota': 'B'},
    {'Nome': 'Lucas', 'Nota': 'A'},
    {'Nome': 'Guilherme', 'Nota': 'A'},
    {'Nome': 'Vinicius', 'Nota': 'B'},
    {'Nome': 'Alisonete', 'Nota': 'C'},
    {'Nome': 'Bruno', 'Nota': 'B'},
    {'Nome': 'Lucas', 'Nota': 'A'},
    {'Nome': 'Guilherme', 'Nota': 'A'},
    {'Nome': 'Vinicius', 'Nota': 'B'},
    {'Nome': 'Alisonete', 'Nota': 'C'},
    {'Nome': 'Bruno', 'Nota': 'B'},
    {'Nome': 'Lucas', 'Nota': 'A'},
    {'Nome': 'Guilherme', 'Nota': 'A'},
    {'Nome': 'Alexandre', 'Nota': 'A'},
    {'Nome': 'Fernanda', 'Nota': 'B'},
    {'Nome': 'Luiz', 'Nota': 'D'},
    {'Nome': 'Guilherme', 'Nota': 'A'},
    {'Nome': 'Alexandre', 'Nota': 'A'},
    {'Nome': 'Fernanda', 'Nota': 'B'},
    {'Nome': 'Luiz', 'Nota': 'D'},
    {'Nome': 'Guilherme', 'Nota': 'A'},
]
ordena = lambda item: item['Nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, agrupados in alunos_agrupados:
    va1, va2 = tee(agrupados) # Função tee imporada para evitar que consuma o iterador
    quant = len(list(va1))
    print(f'{quant} alunos tiraram a nota {agrupamento}')
    for aluno in va2:
        print(f'\t{aluno}') # \t aperta TAB na execução do código (A penas visual)
    print()


