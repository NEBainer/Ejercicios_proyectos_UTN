'''Realizar un menú de opciones en donde el usuario pueda realizar las siguientes operaciones:
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
#Funcion para listar los numeros pares
def listar_pares(par: int) -> int:
    lista_par = []
    lista_par= lista_par[par]
    mensaje = "Los numeros pares ingresados son: "
    for i in range(len(lista_par)):
        mensaje += str(lista_par[i]) + " "
    
    return mensaje

#Funcion para listar los numeros ingresados
def listar_numeros(lista: list) -> str:
    mensaje = "Los numeros ingresados son: "
    for i in range(len(lista)):
        mensaje += str(lista[i]) + " "
    
    return mensaje

#Funcion para determinar el mayor numero impar
def informar_mayor_impar(lista: list) -> int|str:
    bandera = True
    for i in range(len(lista)):
        if lista[i] % 2 != 0 and bandera == True or lista[i] > mayor_impar:
            mayor_impar =lista[i]
            bandera = False
    if bandera == True:
        mensaje = print("No hubo numeros impares")
    else:
        mensaje = print(f"El mayor de los numeros impares es {mayor_impar}")

    return mensaje
#Funcion para sumar los numeros pares
def contar_pares(lista: list) -> int|str:
    acumulador_pares = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            listar_pares(lista[i])
            acumulador_pares += lista[i]
    if acumulador_pares > 0:
        mensaje = print(f"La sumatoria de los numeros pares es {acumulador_pares}")
    else:
        mensaje = print("No se ingresaron numeros pares")
    
    return mensaje

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
    if bandera == False:
        print("No se ingresaron numeros. Ingrese primero a la opcion 1")

#Pedir los numeros
def pedir_diez_numeros(lista: list) -> list:
    for i in range(len(lista)):
        numero = int(input("Ingrese un numero entero entre -1000 y 1000: "))
        while numero < -1000 or numero > 1000:
            numero = int(input("Error, ingrese un numero entero entre -1000 y 1000: "))
        lista[i] = numero
    
    return(lista)

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

    system("pause")
    system("cls")
