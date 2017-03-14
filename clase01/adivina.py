import random

numero = random.randint(1, 10)

while True:
    numero_usuario = int(input('Estoy pensando en un número, cuál es?: '))

    if numero_usuario > numero:
        print('El número es mayor :(')
    elif numero_usuario < numero:
        print('El número es menor :(')
    else:
        print('ACERTASTE!!!')
        break
