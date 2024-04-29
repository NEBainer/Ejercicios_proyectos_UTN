'''FUNCIONES_5 Bainer Ezequiel
Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.'''
def calcular_area():
    radio = input("Ingrese el radio del circulo al cual le quiere calcular el area: ")
    while not radio.isdigit() or radio == " " or radio == None:
        radio = input("Error, ingrese un numero para poder calcular el area: ")

    radio = float(radio)
    area = 3.14 * (radio ** 2)

    return area

area_calculada = calcular_area()
print("El area del circulo es de:", area_calculada)