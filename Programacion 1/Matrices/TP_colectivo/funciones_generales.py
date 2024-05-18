from funciones_especificas import *

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