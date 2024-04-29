# '''1) Realizar una función para pedir un número por consola. La misma deberá seguir el siguiente prototipo En donde:
# mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
# mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido.
# mínimo: valor mínimo admitido (inclusive)
# máximo: valor máximo admitido (inclusive)
# reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.
# En caso de que la función no haya podido conseguir un número válido, la misma retorna None.

# 2) Repetir el mismo procedimiento para un dato de tipo float.

# 3) Teniendo en cuenta la función del punto 1, crear la función get_string. La misma validará la longitud de la cadena ingresada dado el parámetro recibido. El siguiente prototipo es la base para realizar el ejercicio (se puede extender):
# '''


# def get_int(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int) -> int|None:
#     numero = input(mensaje)
#     numero = int(numero)
#     vueltas = 0
#     while numero < minimo or numero > maximo:
#         numero = input(f"Maaaaaaal!! {mensaje_error}")
#         numero = int(numero)
#         vueltas += 1
#         if vueltas == reintentos - 1:
#             return None
#     return numero

# entero = get_int("Ingrese un numero entero entre 1 y 29(3 oportunidades): ", "Error, ingrese un numero entero: ",1, 29, 3) 

# '''def get_float(mensaje:str, mensaje_error:str, minimo:float, maximo:float, reintentos:float) -> float|None:
#     numero = input(mensaje)
#     numero = float(numero)
#     vueltas = 0
#     while numero < minimo or numero > maximo:
#         numero = input(f"Maaaaaaal!! {mensaje_error}")
#         numero = float(numero)
#         vueltas += 1
#         if vueltas == reintentos - 1:
#             return None
#     return numero

# entero = get_float("Ingrese un numero flotante entre 1 y 29(3 oportunidades): ", "Error, ingrese un numero flotante: ",1, 29, 3) 
# print (entero)'''

def get_string(cadena: str, longitud: int) -> str|None:
    dato = input(cadena)
    dato_dos = input(longitud)
    dato_dos = int(dato_dos)
    if len(dato) == dato_dos:
        mensaje = f"La cadena ingresada coincide con la longitud ingresada, es: {dato_dos}"
        return mensaje
    else:
        mensaje = "Error, la longitud no coincide con la cadena"
        return mensaje

string = get_string("Ingrese una cadena de longitud a definir: ", "Ingrese la longitud de la cadena: ")
print (string)