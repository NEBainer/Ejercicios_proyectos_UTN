#Funcion para mostrar la sumatoria de los numeros pares
def contar_pares(lista: list) -> int|str:
    acumulador_pares = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            acumulador_pares += lista[i]
    if acumulador_pares > 0:
        mensaje = print(f"La sumatoria de los numeros pares es {acumulador_pares}")
    else:
        mensaje = print("No se ingresaron numeros pares")
    
    return mensaje

#Funcion para listar los numeros ingresados
def listar_numeros(lista: list) -> str:
    mensaje = "Los numeros ingresados son: "
    for i in range(len(lista)):
        mensaje += str(lista[i]) + " "
    
    return mensaje

#Funcion para listar los numeros pares
def listar_pares(lista: list) -> list:
    bandera = True
    mensaje = "Los numeros pares son: "
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            bandera = False
            mensaje += str(lista[i]) + " "
    if bandera == True:
        mensaje = "No hubo numeros pares"

    return mensaje

#Funcion para listar los numeros impares
def listar_impares(lista: list) -> str|int:
    mensaje = "Los numeros de las posiciones impares son: "
    for i in range(len(lista)):
        if (i-1) % 2 != 0:
            mensaje += str(lista[i]) + " "

    return mensaje