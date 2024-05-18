import random

# Funcion para crear los legajos randoms
def crear_legajos(matriz: list) -> list:
    M = len(matriz)
    N = len(matriz[0])

    for i in range(M):
        for j in range(N):
            matriz[i][j] = random.randint(1, 99)

    return matriz

# Funcion para comprobar que el chofer exista
def comprobar_legajo(lista_a: list, identificacion: int) -> bool:
    for i in range(len(lista_a)):
        for j in range(len(lista_a[i])):
            if identificacion == lista_a[i][j]:
                return True

    return False

# Funcion para cargar la recaudacion
def cargar_recaudacion() -> list:
    verificar_linea = True
    verificar_coche = True
    matriz_lineas_y_coches = [[0] * 5 for _ in range(3)]
    while verificar_linea:
        linea = int(input("Ingrese la linea a la que pertenece: "))
        if linea >= 1 or linea <= 3:
            existe_la_linea = comprobar_linea(matriz_lineas_y_coches, linea)
            verificar_linea = existe_la_linea
            if verificar_linea == True:
                print("Error")
        else:
            print("Error, ingrese una línea válida.")

    while verificar_coche:
        coche = int(input("Ingrese su numero de coche: "))
        if coche >= 1 or linea <= 5:
            existe_el_coche = comprobar_coche(matriz_lineas_y_coches, coche)
            verificar_coche = existe_el_coche
            if verificar_coche == True:
                print("Error")
        else:
            print("Error, ingrese un número de coche válido.")

    recaudacion = int(input("Ingrese la recaudacion que realizó: "))
    matriz_lineas_y_coches[linea - 1][coche - 1] += recaudacion

    return matriz_lineas_y_coches

# Funcion para comprobar que la linea exista
def comprobar_linea(matriz_lineas: list, ingreso: int) -> bool:
    for i in range(len(matriz_lineas)):
        if ingreso == i + 1:
            return False

    return True

# Funcion para comprobar que el coche exista
def comprobar_coche(matriz_coches: list, colectivo: int) -> bool:
    for i in range(len(matriz_coches[0])):
        if colectivo == i + 1:
            return False

    return True

# Funcion para mostrar los elementos de una matriz
def mostrar_matriz(matriz: list) -> str:
    matriz_str = ""
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz_str += f"{matriz[i][j]:5}"
        matriz_str += "\n"

    return matriz_str

# Funcion para cuando no carga primero una planilla
def validar_bandera(bandera: bool) -> str:
    mensaje = ""
    if bandera == False:
        mensaje = print("No se ingresaron numeros. Ingrese primero a la opcion 1")

    return mensaje