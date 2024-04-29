# import validate


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

# def get_float(mensaje:str, mensaje_error:str, minimo:float, maximo:float, reintentos:float) -> float|None:
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
# print (entero)

def get_string(cadena: str, mensaje_error: str, longitud: int, reintentos: int) -> str | None:
    while reintentos > 0:
        dato = input(cadena)
        if len(dato) == longitud:
            mensaje = "La cadena ingresada coincide con la longitud"
            break
        else:
            reintentos -= 1
            mensaje = f"{mensaje_error}{reintentos} intentos"
            print(mensaje)
    if reintentos == 0:
        return None
    else:
        return mensaje
    

string = get_string("Ingrese una cadena de longitud de 5 caracteres: ", "Error, le quedan: ", 5, 3)
print(string)