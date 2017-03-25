def calcular(operando1, operando2, operador='+'):
    if operador == '+':
        return operando1 + operando2
    elif operador == '-':
        return operando1 - operando2
    elif operador == '*':
        return operando1 * operando2
    elif operador == '/':
        return operando1 / operando2

print(calcular(3, 4) + 5)
