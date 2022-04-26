Lista = [
    [1, 4, 3, 2, 6, 5, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [7, 6, 3, 10, 8, 5, 1, 8, 9, 2],
    [10, 9, 8, 7, 5, 6, 2, 3, 4, 1],
    [10, 9, 8, 1, 6, 1, 4, 3, 2, 1],
    [7, 5, 8, 4, 9, 9, 1, 3, 10, 2],
    [9, 6, 5, 5, 5, 2, 7, 10, 4, 1],
    [3, 2, 10, 6, 10, 5, 4, 1, 8, 7],
]

def Encontra_Duplicata(NomeLista=None):
    Contador = 0
    Duplicada_Encontrada = False
    if NomeLista:
      for L in NomeLista:
        for NL in L:
            if NL == L[0] and Duplicada_Encontrada==False:
                if Contador == 0:
                    Contador += 1
                else:
                    Duplicada_Encontrada = True
                    print(NL)
            if NL == L[1] and Duplicada_Encontrada==False:
                if Contador == 0:
                    Contador += 1
                else:
                    Duplicada_Encontrada = True
                    print(NL)
            if NL == L[2] and Duplicada_Encontrada==False:
                if Contador == 0:
                    Contador += 1
                else:
                    Duplicada_Encontrada = True
                    print(NL)
            if NL == L[3] and Duplicada_Encontrada==False:
                if Contador == 0:
                    Contador += 1
                else:
                    Duplicada_Encontrada = True
                    print(NL)
            if NL == L[4] and Duplicada_Encontrada==False:
                if Contador == 0:
                    Contador += 1
                else:
                    Duplicada_Encontrada = True
                    print(NL)
            if NL == L[5] and Duplicada_Encontrada==False:
                if Contador == 0:
                    Contador += 1
                else:
                    Duplicada_Encontrada = True
                    print(NL)
            if NL == L[6] and Duplicada_Encontrada==False:
                if Contador == 0:
                    Contador += 1
                else:
                    Duplicada_Encontrada = True
                    print(NL)
            if NL == L[7] and Duplicada_Encontrada==False:
                if Contador == 0:
                    Contador += 1
                else:
                    Duplicada_Encontrada = True
                    print(NL)
            if NL == L[8] and Duplicada_Encontrada==False:
                if Contador == 0:
                    Contador += 1
                else:
                    Duplicada_Encontrada = True
                    print(NL)
            if NL == L[9] and Duplicada_Encontrada==False:
                if Contador == 0:
                    Contador += 1
                else:
                    Duplicada_Encontrada = True
                    print(NL)
            Contador = 0
        if not Duplicada_Encontrada: print(-1)
        if Duplicada_Encontrada:
            Duplicada_Encontrada = False

Encontra_Duplicata(Lista)


