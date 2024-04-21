'''Realizar una función recursiva que calcule la suma de los primeros números naturales'''

def sumar_naturales(numero: int)->int:
    if numero <= 0:
        resultado = 0
    else:
        resultado = numero + sumar_naturales(numero - 1)
    
    return resultado


natural = sumar_naturales(5)

print(natural)

'''Realizar una función recursiva que calcule la potencia de un número'''

def calcular_potencia(base: int, exponente: int)->int:
    if exponente == 0:
        resultado = 1
    else:
        resultado = base * calcular_potencia(base, exponente -1)

    return resultado

potencia = calcular_potencia(2, 4)

print(potencia)

'''Realizar una función recursiva que la suma de los dígitos de un número'''
def sumar_digitos(numero: int) -> int:
    # Caso base: Si el número tiene un solo dígito, retornamos ese mismo número
    if numero == 0:
        return 0
    # Caso recursivo: Suma el último dígito al resultado de la suma de los dígitos del resto del número
    else:
        ultimo_digito = numero % 10  # Obtenemos el último dígito del número
        resto_numero = numero // 10  # Obtenemos el resto del número sin el último dígito
        return ultimo_digito + sumar_digitos(resto_numero)  # Llamada recursiva con el resto del número

resultado = sumar_digitos(123345531)

print(resultado) 

'''Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La función deberá seguir el siguiente prototipo:

Definición:
La sucesión de Fibonacci comienza con los números 0 y 1, y cada número subsecuente es la suma de los dos anteriores:'''


