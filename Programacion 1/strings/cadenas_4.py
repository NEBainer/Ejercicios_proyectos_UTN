'''Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos.
'''
def suprimir_caracteres_repetidos(cadena: str) -> str:
    nueva_cadena = ""
    
    for i in range(len(cadena)):
        repetido = False
        for j in range(len(nueva_cadena)):
            if cadena[i] == nueva_cadena[j]:
                repetido = True
                break
        
        # Si no está repetido, agregarlo a nueva_cadena
        if repetido == False:
            nueva_cadena += cadena[i]
    
    return nueva_cadena

cadena = input("Ingrese una cadena: ")
cadena_sin_repetidos = suprimir_caracteres_repetidos(cadena)
print(cadena_sin_repetidos)