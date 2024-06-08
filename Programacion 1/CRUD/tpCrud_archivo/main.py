'''
El programa deberá gestionar una lista de hasta 20 empleados. Cada empleado será representado mediante un diccionario.
Si se alcanza el límite de 20 empleados, se deberá notificar al usuario. Solo se podrá ingresar un empleado en caso de que se efectúe una vacante nueva (o sea que se elimine uno).
Al ingresar un empleado, el ID debe ser autoincremental, comenzando en 1. Cada empleado tendrá un ID único.
El resto de los datos deberán ser ingresados por consola.

Validaciones: (LISTOOOOOO)

Opciones del menú:

Ingresar empleado: Pedirá los datos necesarios y dará de alta a un nuevo empleado, asignando un ID autoincremental.
Modificar empleado: Permitirá alterar cualquier dato del empleado excepto su ID. Se usará el ID para identificar al empleado a modificar. Se mostrará un submenú para seleccionar qué datos modificar. Se indicará si se realizaron modificaciones o no.
Eliminar empleado: Eliminará permanentemente a un empleado de la lista original. Se pedirá el ID del empleado a eliminar. 
Mostrar todos: Imprimirá por consola la información de todos los empleados en formato de tabla:

****************************************************
|    Nombre    |   Apellido   |      Puesto      |    Salario     |
—-----------------------------------------------------------
|    German    |   Scarafilo  |     Gerente      |   $500.000 |
|   Giovanni    | Lucchetta  |  Supervisor    |  $300.000 |
****************************************************

Calcular salario promedio: Calculará e imprimirá el salario promedio de todos los empleados.
Buscar empleado por DNI: Permitir al usuario buscar y mostrar la información de un empleado específico ingresando su DNI.
Ordenar empleados: Ofrecer la opción de ordenar y mostrar la lista de empleados por nombre, apellido, o salario de forma ascendente o descendente.
Salir: Terminará la ejecución del programa.

Requisitos adicionales:

El programa deberá estar correctamente modularizado, haciendo uso de módulos, paquetes y funciones propias para solicitar enteros, flotantes y cadenas, así como para las validaciones de cada uno de estos tipos de datos.
El código debe estar programado de manera eficiente y siguiendo buenas prácticas de la programación y las reglas de estilo de la cátedra.

Archivos

Al iniciar el programa, se deberá leer el archivo Empleados.csv para tener la lista de empleados actualizada.
Al finalizar el programa (puede ser en la opción salir) se deberá actualizar el archivo Empleados.csv, con los datos de los empleados.
Los empleados que hayan sido dados de baja deberán guardarse en un archivo Json, llamado “Bajas.json”
La opción 8 del menú, le solicitará al usuario que ingrese un sueldo. El programa deberá generar un reporte con todos los empleados que superen ese sueldo. Una función se encargará de realizar dicha acción, la misma deberá guardar el reporte en un archivo de texto indicando el número de reporte (el programa deberá recordar este dato de alguna forma), la fecha de solicitud del reporte, la cantidad de empleados que coinciden con el criterio y el listado.

La opción 9 del menú, le solicitará al usuario el apellido de un empleado. Realizar un informe con las mismas características que el punto anterior.'''
from os import system
from funciones_principales import *

def mostrar_menu_principal():
    opcion = input("MENU PRINCIPAL\n1. Ingresar empleado\n2. Modificar empleado\n3. Eliminar empleado\n4. Mostrar todos los empleados\n5. Calcular salario promedio\n6. Buscar empleado por DNI\n7. Ordenar empleados\n8. Salir\n")

    return opcion

system("cls")

lista_empleados = [
    {'id': 1, 'nombre': "Eze", 'apellido': "Bainer", 'dni': 5012312, 'puesto': "Analista", 'salario': 10000000},
    {'id': 2, 'nombre': "Maria", 'apellido': "bananitas", 'dni': 9999998, 'puesto': "Gerente", 'salario': 123123123},
    {'id': 3, 'nombre': "Pedro", 'apellido': "Tazo", 'dni': 6912312, 'puesto': "Encargado", 'salario': 800000}
    ]
id = 0
if id == 20:
    mensaje = ("ADVERTENCIA: Lista de empleados llena. No se podra ingresar mas empleados hasta que se genere una vacante.")
    print(mensaje)

while True:
    opcion = mostrar_menu_principal()
    match opcion:
        case "1":
            if id <= 20:
                # id += 1
                lista_empleados = ingresar_empleado(lista_empleados, id)
            else:
                print(mensaje)
        case "2":
            ingreso_de_id = input("Ingrese el id del usuario que desea modificar:\n")
            empleado_modificado = modificar_empleado(lista_empleados, ingreso_de_id)
            print(empleado_modificado)

        case "3":
            eliminar_empleado(lista_empleados, id)
        case "4":
            mostrar_todos_los_empleados(lista_empleados)
    system("pause")
    system("cls")