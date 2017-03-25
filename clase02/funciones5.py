def suma(sumando1, sumando2):
    return sumando1 + sumando2


def resta(sumando1, sumando2):
    return sumando1 - sumando2


def producto(factor1, factor2):
    return factor1 * factor2


def cociente(dividendo, divisor):
    return dividendo / divisor


def obtener_calculador(operacion):
    if operacion == '+':
        return suma
    elif operacion == '-':
        return resta
    elif operacion == '*':
        return producto
    elif operacion == '/':
        return cociente

resultado = obtener_calculador('+')(3, 4)

