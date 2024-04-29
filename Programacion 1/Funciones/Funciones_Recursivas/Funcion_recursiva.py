def calcular_factorial(numero):
    if numero != 0:
        factorial = numero * calcular_factorial(numero - 1)
    else:
        factorial = 1
    
    return factorial

factorial = calcular_factorial(5)

print(factorial)

'''def calcular_factorial(numero):
    if numero == 0:
        factorial = 1
    else:
        factorial = numero * calcular_factorial(numero - 1)

    return factorial'''