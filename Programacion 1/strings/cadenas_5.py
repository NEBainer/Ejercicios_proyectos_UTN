'''Crear una función que reciba una cadena por parámetro y suprima las vocales de la misma.'''
def suprimir_vocales(cadena: str) -> str:
    cadena_sin_vocales = ""

    for i in range(len(cadena)):
            if cadena[i] != "a" and cadena[i] != "e" and cadena[i] != "i" and cadena[i] != "o" and cadena[i] != "u": 
                cadena_sin_vocales += cadena[i]
        
    return cadena_sin_vocales

cadena = input("Ingrese una cadena: ")
cadena_sin_repetidos = suprimir_vocales(cadena)
print(cadena_sin_repetidos)