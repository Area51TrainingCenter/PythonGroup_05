import random

sustantivos = ['perro', 'gato', 'humano', 'unicornio', 'sapo',
               'hormiga', 'camello']
verbos = ['corrió', 'saltó', 'andó', 'voló', 'creció', 'habló',
          'discutió']

oracion = 'El {} {} sobre un {} y se sintió feliz.'

sustantivo_1 = random.choice(sustantivos)
sustantivo_2 = random.choice(sustantivos)
verbo = random.choice(verbos)

print(oracion.format(sustantivo_1, verbo, sustantivo_2))
