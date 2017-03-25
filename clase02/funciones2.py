def calcular(**kwargs):  # keyword arguments
    operador = kwargs.get('operador') or '+'
    operando1 = kwargs['operando1']
    operando2 = kwargs['operando2']

    if operador == '+':
        return operando1 + operando2
    elif operador == '-':
        return operando1 - operando2
    elif operador == '*':
        return operando1 * operando2
    elif operador == '/':
        return operando1 / operando2

print(calcular(operando1=3, operando2=4, nombre='moises'))
