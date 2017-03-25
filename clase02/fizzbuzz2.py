numero = 1

while numero <= 100:
    numero_str = ''
    if numero % 3 == 0:
        numero_str += 'fizz'

    if numero % 5 == 0:
        numero_str += 'buzz'

    print(numero_str or numero)
    numero += 1
