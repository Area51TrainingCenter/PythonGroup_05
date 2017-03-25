def decorar(funcion_suma):
    def decorador(*args):
        print('antes de llamar a la funcion')
        resultado = funcion_suma(*args)
        print('despues de llamar a la funcion')
        return resultado
    return decorador


@decorar
def suma(a, b):
    return a + b

# suma = decorar(suma)


print(suma(3, 5))
