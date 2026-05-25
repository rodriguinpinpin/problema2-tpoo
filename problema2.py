def sumar_recursiva(lista, PI, PF):
    if PI > PF:
        return 0
    else:
        return lista[PI] + sumar_recursiva(lista, PI + 1, PF)

    lista = [2, 4, 6, 3]
    pos_inicial = 2
    pos_final = 3
    
    
    