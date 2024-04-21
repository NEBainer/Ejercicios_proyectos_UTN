'''FUNCIONES_8 Bainer Ezequiel
Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.'''
def calcular_potencia():
    base = input("Ingrese el numero del cual quiere saber la potencia: ")
    while not base.isdigit() or base == None or base == " ":
        base = input("Ingrese un numero valido: ")
    base = int(base)

    exponente = input("Ingrese el numero al cual quiere elevar la base: ")
    while not exponente.isdigit() or exponente == None or exponente == "":
        exponente = input("Ingrese un numero valido: ")
    exponente = int(exponente)

    numero_potenciado = base ** exponente
    return numero_potenciado

numero_final = calcular_potencia()
print ("El resultado de la potenciacion de los numeros ingresados es:", numero_final)

def get_int(mensaje: str, minimo: int, maximo: int) -> int:
    numero = input(mensaje)
    numero = int(numero)
    while numero < minimo or numero > maximo:
        numero = input(f"error{mensaje}")
        numero = int(numero)
    return numero

edad = get_int("Ingrese su edad: ")#15 - 30
legajo = get_int("Ingrese su legajo") # 1500 - 2756
nota = get_int("Ingrese su nota")#1 - 10