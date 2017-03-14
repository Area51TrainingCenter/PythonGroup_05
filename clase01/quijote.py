archivo = open('quijote.txt')
contenido = archivo.read()
archivo.close()

# {'a': 0, 'b': 0, ....}
letras = {}  # <-- Diccionario Vacío

for letra in contenido.lower():
    if letra in 'abcdefghijklmnñopqrstuvwxyz':
        if letra not in letras:
            letras[letra] = 0
        letras[letra] += 1

print(sorted(letras.items(),
             reverse=True,
             key=lambda x: x[1]))
