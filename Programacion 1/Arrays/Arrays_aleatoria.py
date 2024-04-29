mi_lista = [-1] * 5

bandera_seguir = True
while bandera_seguir == True:
    posicion = int(input("Ingrese la posicion: "))
    while posicion < 1 or posicion > len(mi_lista): #El usuario es pelotudo, no va a saber que empezamos en cero los arrays, hay que ponerle el 1 como inicio.
        posicion = int(input("Reingrese un numero menor a 6 y mayor a 0: "))

    if mi_lista[posicion] != -1:
        print(f"La posicion {posicion} ya esta ocupada.")
        
    else:
        numero = int(input("Ingrese un numero: "))
        mi_lista[posicion-1] = numero #Para que no me quede ordenado como el culo le resto a uno asi me queda bien.

    seguir = input("Desea ingresar otro (si/no)?")
    if seguir == "no":
        bandera_seguir = False

for i in range(len(mi_lista)):
    if mi_lista[i] != -1:
        print(f"Posición {i+1} -> {mi_lista[i]}")
