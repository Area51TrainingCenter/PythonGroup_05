from functools import reduce


def suma(a, b):
    return a + b

numeros = range(1, 101)
resultado = reduce(suma, numeros, 0)
# resultado = 0
# resultado = suma(resultado, numeros[0])
# resultado = suma(resultado, numeros[1])
# resultado = suma(resultado, numeros[2])
# ...
print(resultado)


resultado = 0
for numero in numeros:
    resultado += numero

print(resultado)
