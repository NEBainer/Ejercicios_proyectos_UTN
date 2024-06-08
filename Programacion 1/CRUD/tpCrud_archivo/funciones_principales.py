from validaciones import *
from os import system

def crear_empleado(id: int, nombre: str, apellido: str, dni: int, puesto: str, salario: int) -> dict:
    diccionario_empleado = {
        "id": id,
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "puesto": puesto,
        "salario": salario
    }

    return diccionario_empleado

def ingresar_empleado(lista_empleados: list, id: int) -> list:
    nombre = input("Ingrese el nombre: ")
    nombre_validado = validar_nombre(nombre)
    apellido = input("Ingrese el apellido: ")
    apellido_validado = validar_nombre(apellido)
    dni = input("Ingrese el dni: ")
    dni_validado = validar_dni(dni)
    puesto = input("Ingrese el puesto: ")
    puesto_validado = validar_puesto(puesto)
    salario = input("Ingrese el salario: ")
    salario_validado = validar_salario(salario)

    diccionario_empleado = crear_empleado(id, nombre_validado, apellido_validado, dni_validado, puesto_validado, salario_validado)

    lista_empleados.append(diccionario_empleado)
    return lista_empleados

def mostrar_un_empleado(un_empleado: dict):
    print(f"{un_empleado['id']:4}{un_empleado['nombre']:>12}{un_empleado['apellido']:>12}{un_empleado['dni']:10}{un_empleado['puesto']:8}{un_empleado['salario']}")

def mostrar_todos_los_empleados(lista_empleados:list[dict]):
    for empleado in lista_empleados:
        mostrar_un_empleado(empleado)

def mostrar_menu_de_modificacion() -> int:
    dato_a_modificar = input("Ingrese el dato que desea modificar:\n1. Nombre\n2. Apellido\n3. Dni\n4. Puesto\n5. Salario\n6. Salir\n")
    return dato_a_modificar

def modificar_empleado(lista_empleados: list[dict], id: str) -> list[dict]:
    id = int(id)
    system("cls")
    mensaje = " "
    for empleado in lista_empleados:
        if id == empleado["id"]: 
            print("Empleado encontrado.\n")
            bandera = True
            se_modifico = False
            while bandera:
                dato_a_modificar = mostrar_menu_de_modificacion()
                match dato_a_modificar:
                    case "1":
                        nuevo_nombre = input("Ingrese el nuevo nombre: ")
                        nuevo_nombre_validado = validar_nombre(nuevo_nombre)
                        empleado["nombre"] = nuevo_nombre_validado
                        bandera = modificar_otro_dato()
                        se_modifico = True
                    case "2":
                        nuevo_apellido = input("Ingrese el nuevo apellido: ")
                        nuevo_apellido_validado = validar_nombre(nuevo_apellido)
                        empleado["apellido"] = nuevo_apellido_validado
                        bandera = modificar_otro_dato()
                        se_modifico = True
                    case "3":
                        nuevo_dni = input("Ingrese el nuevo dni: ")
                        nuevo_dni_validado = validar_dni(nuevo_dni)
                        empleado["dni"] = nuevo_dni_validado
                        bandera = modificar_otro_dato()
                        se_modifico = True
                    case "4":
                        nuevo_puesto = input("Ingrese el nuevo puesto: ")
                        nuevo_puesto_validado = validar_puesto(nuevo_puesto)
                        empleado["puesto"] = nuevo_puesto_validado
                        bandera = modificar_otro_dato()
                        se_modifico = True
                    case "5":
                        nuevo_salario = input("Ingrese el nuevo salario: ")
                        nuevo_salario_validado = validar_salario(nuevo_salario)
                        empleado["salario"] = nuevo_salario_validado
                        bandera = modificar_otro_dato()
                        se_modifico = True
                    case "6":
                        mensaje = "Saliendo del menu de modificación de empleados...\n"
                        break
                    case _:
                        print("Opción no valida. Por favor ingrese una opción del 1 al 6.\n")
                system("pause")
                system("cls")
            if se_modifico == False:
                mensaje += "No se modifico ningun dato de los empleados"
                return mensaje
            else:
                mensaje += "Se modificaron datos de los empleados"
                return mensaje
    mensaje += "No se encontraron empleados con el ID ingresado."
    return mensaje

def eliminar_empleado(lista_empleados: list[dict], id: int):
    eliminado = None 
    for empleado in lista_empleados:
        if id == empleado["id"]:
            eliminado = empleado
            break
    if eliminado != None:
        lista_empleados.remove(eliminado)

def calcular_salario_promedio(lista_empleados: list[dict]) -> float:
    acumulador_de_salarios = 0
    for empleado in lista_empleados:
        acumulador_de_salarios = acumulador_de_salarios + empleado["salario"]
    promedio_de_salarios = float(acumulador_de_salarios / len(lista_empleados))
    return promedio_de_salarios

def buscar_empleado_por_dni(lista_empleados: list[dict], dni = int) -> dict:
    encontrado = None
    for empleado in lista_empleados:
        if dni == empleado["dni"]:
            encontrado = empleado
        break
    if encontrado != None:
        mostrar_un_empleado(empleado)

def mostrar_menu_de_ordenamiento() -> str:
    tipo_de_ordenamiento = input("De que manera desea ordenar la lista de empleados?\n1. Ordenar por nombre\n2. Ordenar por apellido\n3. Ordenar por salario de manera ascendente\n4. Ordenar por salario de manera descendente\5. Dejar la lista de empleados como está.")
    return tipo_de_ordenamiento

def ordenar_lista(lista_empleados: list ,parametro: str) -> list[dict]:
    for empleado in range(0, len(lista_empleados)-1):
        for j in range(empleado + 1, len(lista_empleados)):
            if lista_empleados[empleado][parametro] > lista_empleados[j][parametro]:
                auxiliar = lista_empleados[empleado][parametro] 
                lista_empleados[empleado][parametro] = lista_empleados[j][parametro] 
                lista_empleados[j][parametro] = auxiliar

def ordenar_lista_descendente(lista_empleados: list ,parametro: str) -> list[dict]:
    for empleado in range(0, len(lista_empleados)-1):
        for j in range(empleado + 1, len(lista_empleados)):
            if lista_empleados[empleado][parametro] < lista_empleados[j][parametro]:
                auxiliar = lista_empleados[empleado][parametro] 
                lista_empleados[empleado][parametro] = lista_empleados[j][parametro] 
                lista_empleados[j][parametro] = auxiliar

def ordenar_empleados(lista_empleados: list[dict]) -> list[dict]:
    while True:
        tipo_de_ordenamiento = mostrar_menu_de_ordenamiento()
        match tipo_de_ordenamiento:
            case "1":
                orden_por_nombre = ordenar_lista(lista_empleados, "nombre")
                mostrar_todos_los_empleados(orden_por_nombre)
            case "2":
                orden_por_apellido = ordenar_lista(lista_empleados, "apellido")
                mostrar_todos_los_empleados(orden_por_apellido)
            case "3":
                orden_por_salario_ascendente = ordenar_lista(lista_empleados, "salario")
                mostrar_todos_los_empleados(orden_por_salario_ascendente)
            case "4":
                orden_por_salario_descendente = ordenar_lista_descendente(lista_empleados, "salario")
                mostrar_todos_los_empleados(orden_por_salario_descendente)
