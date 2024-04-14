'''FUNCIONES_2 Bainer Ezequiel
Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.'''

def pedir_numero_flotante():
    numero = None
    while numero == None: 
        entrada = input("Ingrese un numero flotante: ")
        if entrada:
            numero = float(entrada)
        else:
            print("Error, ingrese un numero flotante: ")

    return numero

numero_flotante = pedir_numero_flotante()
print ("El numero ingresado es:", numero_flotante)