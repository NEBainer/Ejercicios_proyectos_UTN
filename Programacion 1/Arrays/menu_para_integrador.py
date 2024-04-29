from os import system
def sumar_numeros(un_numero, otro_numero):
    suma = un_numero + otro_numero

    return suma

bandera_ingreso = False
bandera_seguir = True
while bandera_seguir == True:
    opcion = int(input("1.Ingresar numeros \n2.Sumar\n3.Restar\n4.Salir\nElija una opcion: "))

    match opcion:
        case 1:
            primer_numero = int(input("Ingrese un numero: "))
            segundo_numero = int(input("Ingrese un numero: "))
            bandera_ingreso = True
        case 2:
            if bandera_ingreso == True:
                suma = sumar_numeros(primer_numero, segundo_numero)
                print(f"La suma es: {suma}")
            else:
                print("No se ingresaron los valores. Ingrese primero a la opcion 1")
        case 3:
            print("Restando numeros")
        case 4:
            bandera_seguir = False

    system("pause")
    system("cls")