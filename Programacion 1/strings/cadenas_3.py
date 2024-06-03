'''Crear una función que reciba como parámetro una cadena y determine si la misma es o no un palíndromo. Deberá retornar un valor booleano indicando lo sucedido.'''
def determinar_palindromo(cadena: str) -> bool:
    cadena_invertida = cadena[::-1] #De esta forma invertimos la cadena
    if cadena != cadena_invertida:
        return False
    else:
        return True

cadena = input("Ingrese una cadena: ")
palindromo = determinar_palindromo(cadena)
print(palindromo)