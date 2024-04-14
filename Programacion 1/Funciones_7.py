'''FUNCIONES_7 Bainer Ezequiel
Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.'''

def encontrar_numero_maximo():
    numero_uno = input("Ingrese el primer numero: ")
    while not numero_uno.isdigit() or numero_uno == " " or numero_uno == None:
        numero_uno = input("Error, ingrese un numero: ")
    
    numero_uno = int(numero_uno)

    numero_dos = input("Ingrese el segundo numero: ")
    while not numero_dos.isdigit() or numero_dos == " " or numero_dos == None:
        numero_dos = input("Error, ingrese un numero: ")
    
    numero_dos = int(numero_dos)

    numero_tres = input("Ingrese el tercer numero: ")
    while not numero_tres.isdigit() or numero_tres == " " or numero_tres == None:
        numero_tres = input("Error, ingrese un numero: ")
    
    numero_tres = int(numero_tres)

    if numero_uno > numero_dos and numero_uno > numero_tres:
        return numero_uno
    elif numero_dos > numero_tres:
        return numero_dos
    else:
        return numero_tres

numero_maximo = encontrar_numero_maximo()
print("El numero maximo ingresado es:", numero_maximo)