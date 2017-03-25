import requests

origen = input('moneda de origen: ')
destino = input('moneda de destino: ')
cantidad = float(input('cantidad a convertir: '))

response = requests.get(
    'http://api.fixer.io/latest',
    params={'base': origen}
)
cambio = response.json()['rates'][destino]

resultado = cantidad * cambio
print('resultado: {}'.format(resultado))
