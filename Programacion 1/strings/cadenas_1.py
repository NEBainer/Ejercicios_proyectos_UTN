'''Crear una función que reciba como parámetro una cadena y determine la cantidad de vocales que hay de cada una (individualmente). La función retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2 la cantidad.
Por ej:
cadena = “murcielaguito”'''

def determinar_cantidad_de_vocales(cadena: str , vocales: list) -> list:
    for i in range(len(vocales)):
        for j in range(len(cadena)):
            if vocales[i][0] == cadena[j]:
                vocales[i][1] += 1
    
    return vocales

def mostrar_cantidad_de_vocales(vocales: list):
    for i in range(len(vocales)):
        for j in range(len(vocales[0])):
            print(f"{vocales[i][j]:2}", end = "")
        print("")

palabra = input("Ingrese la cadena a la cual le quiere determinar la cantidad de vocales: ")
vocales = [["a",0],
            ["e",0],
            ["i",0],
            ["o",0],
            ["u",0]]

determinar_cantidad_de_vocales(palabra, vocales)
mostrar_cantidad_de_vocales(vocales)

#OTRA MANERA MAS COMPLICADA DE HACERLO
def contar_vocales(cadena):
    vocales_validas = ["a","e","i","o","u"]
    count_v = [0] * len(vocales_validas)

    for i in range(len(cadena)):
        caracter = cadena[i]
        for j in range(len(vocales_validas)):
            vocal = vocales_validas[j]
            if caracter == vocal:
                count_v[j] += 1

    return vocales_validas, count_v

cadena = "Murcielaguito"
resultado = contar_vocales(cadena)
print(resultado, end = " ")