'''Crear una función que reciba una cadena y un caracter. La función deberá devolver el índice en el que se encuentre la primera incidencia de dicho caracter, o -1 en caso de que no esté.'''
def devolver_indice(cadena: str, caracter: str) -> int:
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            mensaje = f"El indice en el que se encuentra la primera incidencia del caracter es: {i+1}"
            return mensaje

    return -1

cadena = input("Ingrese una cadena: ")
caracter = input("Ingrese un caracter: ")
indice_del_caracter = devolver_indice(cadena, caracter)
print(indice_del_caracter)