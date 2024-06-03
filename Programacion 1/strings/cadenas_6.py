'''Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena.'''
def contar_subcadena(cadena: str, subcadena: str) -> int:
    contador = 0
    longitud_subcadena = len(subcadena)
    longitud_cadena = len(cadena)

    for i in range(longitud_cadena - longitud_subcadena + 1): #Con el +1 nos aseguramos que recorra la totalidad de la cadena en donde pueda haber una longitud igual a la subcadena
        if cadena[i:i + longitud_subcadena] == subcadena: #De esta manera recorre toda la cadena hasta el limite de la misma sin irse de rango
            contador += 1

    return contador

cadena = input("Ingrese una cadena: ")
subcadena = input("Ingrese la subcadena a buscar: ")

resultado = contar_subcadena(cadena, subcadena)
print(f"La subcadena '{subcadena}' aparece {resultado} veces en la cadena.")