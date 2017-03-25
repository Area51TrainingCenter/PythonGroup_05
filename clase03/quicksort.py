def quicksort(lista):
    if len(lista) == 0:
        return []
    if len(lista) == 1:
        return lista

    primer_elemento = lista[0]
    resto = lista[1:]
    menores = [numero for numero in resto if numero < primer_elemento]
    mayores = [numero for numero in resto if numero > primer_elemento]
    # mayores = []
    # for numero in resto:
    #     if numero > primer_elemento:
    #         mayores.append(numero)
    return quicksort(menores) + [primer_elemento] + quicksort(mayores)


print(quicksort([13, 7, 8, 4, 55]))
