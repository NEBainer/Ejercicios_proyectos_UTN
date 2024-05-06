''' Una empresa de colectivos tiene 3 líneas de 5 coches cada una. En total tiene 15 choferes (cada uno con un legajo distinto generado aleatoriamente).
Nos piden desarrollar un software que presente el siguiente menú  de usuarios:
Menú:
1)Cargar planilla. El chofer se debe identificar (el legajo debe existir dentro de una matriz de legajos). Si el chofer existe cargará la recaudación del viaje indicando línea y coche (no necesariamente un chofer está asignado a una única línea y coche), estos datos deben estar validados. Un chofer puede cargar más de una recaudación por día (para distintas líneas y distintos coches). Cada coche de cada línea puede tener varias recaudaciones diarias.
2)Mostrar la recaudación de cada coche y línea.
3)Calcular y mostrar recaudación por línea.
4)Calcular y mostrar recaudación por coche.
5)Calcular y mostrar la recaudación total.
6)Salir
Todo el desarrollo tiene que estar modularizado: ingreso de datos, validaciones de líneas y coches, generación y verificación de existencia de legajo, cálculos, etc.
'''

from os import system
import random

# Funcion para crear los legajos randoms
def crear_legajos(matriz: list) -> list:
    M = len(matriz)
    N = len(matriz[0])

    for i in range(M):
        for j in range(N):
            matriz[i][j] = random.randint(1, 99)

    return matriz

# 1)Funcion para cargar planilla
def cargar_planilla(lista: list) -> list:
    legajo_valido = True
    while legajo_valido:
        legajo = int(input("Ingrese su legajo: "))
        comprobar_chofer = comprobar_legajo(lista, legajo)
        if comprobar_chofer == True:
            legajo_valido = False
        else:
            print("Error, ingrese un legajo correcto: ")

    return cargar_recaudacion()

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

# 2)Mostrar la recaudación de cada coche y línea.
def acumular_recaudaciones(matriz_acumulable: list, recaudaciones: list) -> list:
    for i in range(len(matriz_acumulable)):
        for j in range(len(matriz_acumulable[0])):
            matriz_acumulable[i][j] += recaudaciones[i][j]

    return matriz_acumulable

# 3)Calcular y mostrar la recaudación por línea.
def mostrar_recaudacion_linea(matriz: list) -> list:
    acumulador_primer_linea = 0
    acumulador_segunda_linea = 0 
    acumulador_tercera_linea = 0 

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == 0:
                acumulador_primer_linea += int(matriz[i][j])
            elif i == 1:
                acumulador_segunda_linea += int(matriz[i][j])
            else:
                acumulador_tercera_linea += int(matriz[i][j])
    resultado = "Recaudacion por linea:\n"
    resultado += f"Linea 1: {acumulador_primer_linea}\n"
    resultado += f"Linea 2: {acumulador_segunda_linea}\n"
    resultado += f"Linea 3: {acumulador_tercera_linea}\n"
    return resultado

#4)Calcular y mostrar la recaudación por coche
def mostrar_recaudacion_coche(matriz: list) -> int:
    acumulador_primer_coche = 0 
    acumulador_segundo_coche = 0 
    acumulador_tercer_coche = 0 
    acumulador_cuarto_coche = 0
    acumulador_quinto_coche = 0

    for j in range(len(matriz[0])):
        for i in range(len(matriz)):
            if j == 0:
                acumulador_primer_coche += int(matriz[i][j])
            elif j == 1:
                acumulador_segundo_coche += int(matriz[i][j])
            elif j == 2:
                acumulador_tercer_coche += int(matriz[i][j])
            elif j == 3:
                acumulador_cuarto_coche += int(matriz[i][j])
            else:
                acumulador_quinto_coche += int(matriz[i][j])
    resultado = "Recaudacion por coche:\n"
    resultado += f"coche 1: {acumulador_primer_coche}\n"
    resultado += f"coche 2: {acumulador_segundo_coche}\n"
    resultado += f"coche 3: {acumulador_tercer_coche}\n"
    resultado += f"coche 4: {acumulador_cuarto_coche}\n"
    resultado += f"coche 5: {acumulador_quinto_coche}\n"
    return resultado

#5)Funcion para mostrar y calcular la recaudacion total
def mostrar_recaudacion_total(matriz: list) -> int:
    recaudacion = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            recaudacion += int(matriz[i][j])
    resultado = f"La recaudacion total fue de: {recaudacion}"
    return resultado

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

matriz_de_legajos = [[0] * 3 for _ in range(5)]
matriz_de_legajos = crear_legajos(matriz_de_legajos)
matriz_acumulable = [[0] * 5 for _ in range(3)]

bandera_ingreso = False
bandera_seguir = True
while bandera_seguir == True:
    menu_de_opciones = int(input(
        "1.Cargar planilla. \n2.Mostrar la recaudación de cada coche y línea. \n3.Calcular y mostrar la recaudación por línea. \n4.Calcular y mostrar la recaudación por coche. \n5.Calcular y mostrar la recaudación total. \n6.Salir\nElija una opcion: "))
    print(matriz_de_legajos)

    match menu_de_opciones:
        case 1:
            planilla_a_cargar = cargar_planilla(matriz_de_legajos)
            matriz_acumulable = acumular_recaudaciones(matriz_acumulable, planilla_a_cargar)
            bandera_ingreso = True
        case 2:
            if bandera_ingreso == True:
                recaudacion_coche_linea = mostrar_matriz(matriz_acumulable)
                print(f"La recaudación de cada coche y linea es: \n{recaudacion_coche_linea}")
            else:
                validar_bandera(bandera_ingreso)
        case 3:
            if bandera_ingreso == True:
                recaudacion_por_linea = mostrar_recaudacion_linea(matriz_acumulable)
                print(recaudacion_por_linea)
            else:
                validar_bandera(bandera_ingreso)
        case 4:
            if bandera_ingreso == True:
                recaudacion_por_coche = mostrar_recaudacion_coche(matriz_acumulable)
                print(recaudacion_por_coche)
            else:
                validar_bandera(bandera_ingreso)
        case 5:
            if bandera_ingreso == True:
                recaudacion_total = mostrar_recaudacion_total(matriz_acumulable)
                print(recaudacion_total)
            else:
                validar_bandera(bandera_ingreso)
        case 6:
            print("Saliendo del programa...")
            bandera_seguir = False
            
    system("pause")
    system("cls")