'''FUNCIONES_1
Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne. Bainer Ezequiel'''

def pedir_numero_entero():
    numero = None
    while numero == None: 
        entrada = input("Ingrese un numero entero: ")
        if entrada.isdigit():
            numero = int(entrada)
        else:
            print("Error, ingrese un numero entero: ")

    return numero

numero_entero = pedir_numero_entero()
print ("El numero ingresado es:", numero_entero)
