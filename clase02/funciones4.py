def suma(sumando1, sumando2):
    return sumando1 + sumando2


def calcular(operacion, operando1, operando2):
    return operacion(operando1, operando2)

print(calcular(suma, 3, 4))
