'''FUNCIONES_1
Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne. Bainer Ezequiel'''

def pedir_numero_entero():
    
    while True: 
        entrada = input("Ingrese un numero entero: ")
        if entrada.isdigit():
            entrada = int(entrada)
            return entrada
        else:
            print("Error, ingrese un numero entero: ")

    

numero_entero = pedir_numero_entero()
print ("El numero ingresado es:", numero_entero)
