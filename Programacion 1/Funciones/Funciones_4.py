'''FUNCIONES_4 Bainer Ezequiel
Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.'''

def pedir_numero_entero():
    numero = None
    while numero == None: 
        entrada = input("Ingrese un numero entero: ")
        if entrada.isdigit():
            numero = int(entrada)
        else:
            print("Error, ingrese un numero entero: ")

    return numero

def pedir_numero_flotante():
    numero = None
    while numero == None: 
        entrada = input("Ingrese un numero flotante: ")
        if entrada:
            numero = float(entrada)
        else:
            print("Error, ingrese un numero flotante: ")

    return numero

def pedir_cadena():
    entrada = input("Ingrese una cadena: ")
    while entrada == None or entrada == "":
        entrada = input("Ingrese una cadena: ")

    return entrada

numero_entero = pedir_numero_entero()
print ("El numero ingresado es:", numero_entero)

numero_flotante = pedir_numero_flotante()
print ("El numero ingresado es:", numero_flotante)

cadena = pedir_cadena()
print ("La cadena ingresada es:", cadena)