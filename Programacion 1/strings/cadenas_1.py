'''Crear una función que reciba como parámetro una cadena y determine la cantidad de vocales que hay de cada una (individualmente). La función retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2 la cantidad.
Por ej:
cadena = “murcielaguito”'''

def determinar_cantidad_de_vocales(cadena: str) -> list:
    vocales = ["a", "e", "i", "o", "u"]
    contador_de_vocales = [0] *5

    for i in range(len(cadena)):
        for j in range(len(matriz[0])):
            if cadena[i] == matriz[0]:
                matriz[i][j] += 1

    return matriz[j]


palabra = input("Ingrese la cadena a la cual le quiere determinar la cantidad de vocales: ")
vocales = determinar_cantidad_de_vocales(palabra)
print(vocales)
