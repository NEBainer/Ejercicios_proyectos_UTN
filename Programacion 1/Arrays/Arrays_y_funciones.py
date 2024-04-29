def mostrar_lista(lista: list, ilogico: int) -> bool:
    exito = False
    if type(lista) == list and type(ilogico) == int:
        exito = True
        for i in range(len(lista)):
            if not verificar_lugar(lista[i], ilogico):
                print(lista[i])

    return exito

def verificar_lugar(valor, ilogico: int) -> bool|None: #Con ilogico se refiere al valor inicial de los elementos dentro del array, osea el -1
    exito = None
    if type(valor) == int and type(ilogico) == int:
        exito = False
        if valor == ilogico:
            exito = True

    return exito

def responder_salir(mensaje: str) -> bool:
    bandera = False
    seguir = input(mensaje)
    if seguir == "si":
        bandera = True
    return bandera


def get_int(mensaje, min, max):
    pass


def cargar_lista_aleatoria(lista:list) -> int:
    bandera_seguir = True
    while bandera_seguir == True:
        posicion = get_int("Ingrese la posicion", 1, len(lista))
        
        retorno = verificar_lugar(lista[posicion-1], -1)
        
        if retorno == True:
            numero = get_int("Ingrese un numero: ", 1, 1000)
            lista[posicion-1] = numero
        elif retorno == False:
            print("El elemento ya esta ocupado")
        else:
            print("Paramentros incorrectos")
            
        bandera_seguir = responder_salir("Queres ingresar otro si/no?")


mi_lista = [-1] * 5


cargar_lista_aleatoria(mi_lista)


if not mostrar_lista(mi_lista):  
    print("Error, no se recibio una lista como parametro")
#Esto quiere decir que si no pudo mostrar la lista por que el parametro recibido por la funcion fue otra que no sea una lista, va a tirar el error de abajo