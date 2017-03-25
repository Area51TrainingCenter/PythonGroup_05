def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

print(factorial(5))

# factorial(5) => 5 * factorial(4)
# factorial(4) => 4 * factorial(3)
# factorial(3) => 3 * factorial(2)
# factorial(2) => 2 * factorial(1)
# factorial(1) => 1 * factorial(0)
# factorial(0) => 1

