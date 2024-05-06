#Pedir los numeros
def pedir_diez_numeros(lista: list) -> list:
    for i in range(len(lista)):
        numero = int(input("Ingrese un numero entero entre -1000 y 1000: "))
        while numero < -1000 or numero > 1000:
            numero = int(input("Error, ingrese un numero entero entre -1000 y 1000: "))
        lista[i] = numero
    
    return(lista)