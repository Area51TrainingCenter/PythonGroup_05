def calcular(operador, operando1, operando2):
    if operador == '+':
        return operando1 + operando2
    elif operador == '-':
        return operando1 - operando2
    elif operador == '*':
        return operando1 * operando2
    elif operador == '/':
        return operando1 / operando2

# operaciones = '+-*/'
operaciones = ['+', '-', '*', '/']

for operacion in operaciones:
    print(calcular(operacion, 3, 5))
