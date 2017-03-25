def fizz_buzz(numero):
    numero_str = ''

    if numero % 3 == 0:
        numero_str += 'fizz'

    if numero % 5 == 0:
        numero_str += 'buzz'

    return numero_str or str(numero)

lista_fizzbuzz = map(fizz_buzz, range(1, 101))
# lista_fizzbuzz = [fizz_buzz(numero) for numero in range(1, 101)]
print('\n'.join(lista_fizzbuzz))
