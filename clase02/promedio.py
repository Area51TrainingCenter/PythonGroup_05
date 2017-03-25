def promedio(*numeros):
    suma = sum(numeros)
    cantidad_elementos = len(numeros)
    return suma / cantidad_elementos

print(promedio(17, 20, 13, 11))
