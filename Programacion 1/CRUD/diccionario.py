'''CREATE'''
def crear_alumno(dni: int, nombre: str, apellido: str, nota: int) -> dict:
    diccionario_alumno = {
        "dni" : dni,
        "nombre" : nombre,
        "apellido" : apellido,
        "nota" : nota
        #"estado": True o False. El profe llamo a esto baja logica. Sirve para determinar si esta dado de baja el usuario o no. Se planteo este tema en la parte de eliminar amigo asi que habria que poner el cambio de estado ahi en tal caso
    }

    return diccionario_alumno

def ingresar_alumno_lista(lista_alumnos: list): #Retorne si pudo o no pudo cargar datos a la lista
    dni = int(input("Ingrese el DNI: "))
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    nota = int(input("Ingrese nota: "))

    diccionario_alumno = crear_alumno(dni, nombre, apellido, nota)

    lista_alumnos.append(diccionario_alumno)

'''READ'''
def mostrar_un_alumno(un_alumno: dict):
    print(f"{un_alumno['dni']:10}{un_alumno['nombre']:>12}{un_alumno['apellido']:>12}{un_alumno['nota']:>4}")

def mostrar_todos_los_alumnos(lista_alumnos:list[dict]):
    for alumno in lista_alumnos:
        mostrar_un_alumno(alumno)

'''UPDATE'''
#GERTIP: Todo lo que modifiquemos no hacerlo sobre la instancia(En este caso alumno). Hacer una copia, modificar esa nota y una vez estamos seguro de que el usuario hizo todo lo que tenia que hacer, recien ahi vuelco el dato que modifique al alumno. Tratar de trabajar con un auxiliar asi no manoseamos el diccionario. Tratar de trabajar con un rollback por si el usuario se arrepiente de algun cambio
def modificar_alumno(lista_alumnos: list[dict], dni: int):
    for alumno in lista_alumnos:
        if dni == alumno["dni"]:  #Recordar usar la variable de iteracion en estos casos y no lo que estoy recorriendo o va a tirar error
            print("Alumno encontrado")
            nueva_nota = int(input("Ingrese la nueva nota: "))
            alumno["nota"] = nueva_nota
            break #Por que o sino va a seguir iterando hasta que termine la lista, independientemente de si encontro al buscado

'''DELETE'''
#A EL PROFE NO LE GUSTA QUE BORREMOS COSAS DENTRO DE EL FOR, HACERLO MEDIANTE ALGORITMO DE BUSQUEDA.
def eliminar_alumno(lista_alumnos: list[dict], dni: int):
    eliminado = None #Hacemos que la variable sea mas global
    for alumno in lista_alumnos:
        if dni == alumno["dni"]:
            eliminado = alumno
            break
    if eliminado != None:
        lista_alumnos.remove(eliminado)
