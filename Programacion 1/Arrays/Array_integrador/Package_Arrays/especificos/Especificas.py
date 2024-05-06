#Funcion para determinar la cantidad de negativos y positivos
def mostrar_positivos_negativos(lista: list) -> str|int:
    contador_positivos = 0
    contador_negativos = 0
    for i in range(len(lista)):
        if lista[i] < 0:
            contador_negativos += 1
        else:
            contador_positivos += 1

    mensaje = print(f"La cantidad de numeros positivos es {contador_positivos} y la cantidad de numeros negativos es {contador_negativos}")
    return mensaje

#Funcion para cuando se saltea la opcion 1
def validar_bandera(bandera: bool) -> str:
    mensaje = ""
    if bandera == False:
        mensaje = print("No se ingresaron numeros. Ingrese primero a la opcion 1")

    return mensaje

#Funcion para determinar el mayor numero impar
def informar_mayor_impar(lista: list) -> int|str:
    mayor_impar = None
    for i in range(len(lista)):
        if lista[i] % 2 != 0 and (mayor_impar == None or lista[i] > mayor_impar):
            mayor_impar =lista[i]

    if mayor_impar == None:
        mensaje = print("No hubo numeros impares")
    else:
        mensaje = print(f"El mayor de los numeros impares es {mayor_impar}")

    return mensaje