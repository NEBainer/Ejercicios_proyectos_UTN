'''def sumar_numeros_2():
    un_numero = input("Ingrese un numero: ")
    un_numero = int(un_numero)
    otro_numero = input("Ingrese otro numero: ")
    otro_numero = int(otro_numero)

    suma = un_numero + otro_numero

    return suma

def sumar_numeros_3(un_numero, otro_numero):
    suma = un_numero + otro_numero

    print(f"La suma es {suma}")

def sumar_numeros_4(un_numero, otro_numero):
    suma = un_numero + otro_numero

    return suma'''

'''def es_par(numero):
    if numero % 2 == 0:
        print("El numero ingresado es par")
    else:
        print("El numero ingresado es impar")

numero = input("Ingrese un numero a verificar si es par")
numero = int(numero)
es_par(numero)'''

numero = input("Ingrese un numero: ")
numero = int(numero)

def es_par(numero):
    if numero % 2 == 0:
        print("El numero es par")
    else:
        print("El número es impar")

es_par(numero)