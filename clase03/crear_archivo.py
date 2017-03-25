nombre = input('Cuál es tu nombre?: ')
archivo = open('nombre.txt', 'w')
archivo.write('tu nombre es {}'.format(nombre))
archivo.close()
