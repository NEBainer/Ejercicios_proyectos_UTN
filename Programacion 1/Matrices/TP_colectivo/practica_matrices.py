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
from funciones_especificas import *
from funciones_generales import *

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