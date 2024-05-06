''' Bainer Ezequiel TURNO NOCHE
Realizar un menú de opciones en donde el usuario pueda realizar las siguientes operaciones:
Pedir el ingreso de 10 números enteros entre -1000 y 1000. 
Mostrar la cantidad de números positivos y negativos.
Mostrar la sumatoria de los números pares.
Informar el mayor de los números impares.
Listar todos los números ingresados.
Listar todos los números pares.
Listar los números de las posiciones impares.  
Salir
Notas:
Solo se podrá ingresar a las opciones b a g, siempre y cuando el usuario haya ingresado los datos solicitados.
Todas las opciones deberán ser programadas en funciones: habrá funciones específicas (por ejemplo para determinar si un número es positivo o negativo) y funciones de nivel general (por ejemplo una función que liste los números pares). Tener en cuenta las características de la programación funcional.
Las funciones específicas deberán estar en el módulo “Especificas.py”, mientras que las generales en el módulo “Array_Generales.py”. Todos estos módulos deben estar integrados en el paquete Package_Arrays.
Utilizar las funciones input del paquete Package_Input.
Consejo: Primero realizar el desarrollo de las funciones y probarlas. Luego, armar los módulos y paquetes.'''

from os import system
from Package_Input.Input import pedir_diez_numeros
from Generales.Array_generales import *
from especificos.Especificas import *

bandera_ingreso = False
mi_lista = [0] * 10
bandera_seguir = True
while bandera_seguir == True:
    opcion = int(input("1.Ingresar 10 numeros enteros entre -1000 y 1000 \n2.Mostrar la cantidad de numeros positivos y negativos\n3.Mostrar la sumatoria de los números pares.\n4.Informar el mayor de los números impares.\n5.Listar todos los números ingresados.\n6.Listar todos los números pares.\n7Listar los números de las posiciones impares.\n8.Salir\nElija una opcion: "))

    match opcion:
        case 1:
            numeros = pedir_diez_numeros(mi_lista)
            bandera_ingreso = True
        case 2:
            if bandera_ingreso == True:
                mostrar_positivos_negativos(mi_lista)
            validar_bandera(bandera_ingreso)
        case 3:
            if bandera_ingreso == True:
                contar_pares(mi_lista)
            validar_bandera(bandera_ingreso)
        case 4:
            if bandera_ingreso == True:
                informar_mayor_impar(mi_lista)
            validar_bandera(bandera_ingreso)
        case 5:
            if bandera_ingreso == True:
                ingresos = listar_numeros(mi_lista)
                print(ingresos)
            validar_bandera(bandera_ingreso)
        case 6:
            if bandera_ingreso == True:
                ingresos_pares = listar_pares(mi_lista)
                print(ingresos_pares)
            validar_bandera(bandera_ingreso)
        case 7:
            if bandera_ingreso == True:
                ingresos_impares = listar_impares(mi_lista)
                print(ingresos_impares)
            validar_bandera(bandera_ingreso)
        case 8:
            mensaje = "Saliendo del programa..."
            print(mensaje)
            break

    system("pause")
    system("cls")
