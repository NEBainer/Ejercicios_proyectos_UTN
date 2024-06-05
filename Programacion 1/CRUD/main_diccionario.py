from diccionario import *
from os import system
'''CREATE'''
'''Para probar primer funcion en donde creamos un alumno'''
# d = crear_alumno(3, "Pedro", "Gomez", 7)
# print(d)

'''Para probar la segunda en donde ingresamos el alumno a una lista con sus respectivos datos'''
# lista = [] #Una buena sugerencia que dio el profe, llamar a esta funcion si y solo si hay lugar en la lista
# ingresar_alumno_lista(lista)
# print(lista)

'''READ'''
'''Para probar la tercer funcion que muestra un alumno'''
# Lista harcodeada para probar la funcion
# lista = [    
#     {'dni': 3, 'nombre': "Pepe", 'apellido': "Gomez", 'nota': 10},
#     {'dni': 10, 'nombre': "Juan", 'apellido': "Gutierrez", 'nota': 4},4

#     {'dni': 5, 'nombre': "Eze", 'apellido': "Bainer", 'nota': 7}
# ]
# mostrar_un_alumno(lista[0])
'''Para probar la cuarta funcion que muestra todos los alumnos'''
# mostrar_todos_los_alumnos(lista)

'''UPDATE'''
'''Para probar la quinta funcion que modifica la nota de un alumno buscandolo primero por dni'''
# modificar_alumno(lista, 10)

'''DELETE'''
# eliminar_alumno(lista, 3)
# mostrar_todos_los_alumnos(lista)


def mostrar_menu():
    opcion = input("MENU\n1. Cargar\n2. Modificar\n3. Eliminar\n4. Mostrar\n5. Salir\n Elija una opcion: ")
    return opcion

system("cls") #Ponemos un clear aca para que borre la ruta que siempre aparece cuando hacemos print de la pantalla
lista_alumnos = [
    {'dni': 3, 'nombre': "Pepe", 'apellido': "Gomez", 'nota': 10},
    {'dni': 10, 'nombre': "Juan", 'apellido': "Gutierrez", 'nota': 4},
    {'dni': 5, 'nombre': "Eze", 'apellido': "Bainer", 'nota': 7}
]
while True:
    opcion = mostrar_menu()
    match opcion:
        case "1":
            ingresar_alumno_lista(lista_alumnos)
        case "2":
            dni = int(input("Ingrese el dni: "))
            modificar_alumno(lista_alumnos, dni)
        case "3":
            pass
        case "4":
            mostrar_todos_los_alumnos(lista_alumnos)
        case "5":
            break
    system("pause")
    system("cls")