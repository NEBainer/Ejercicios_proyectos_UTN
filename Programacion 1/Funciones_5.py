'''FUNCIONES_5 Bainer Ezequiel
Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.'''
def calcular_area():
    area = input("Ingrese el radio del circulo al cual le quiere calcular el area: ")
    while not area.isdigit() or area == " " or area == None:
        area = input("Error, ingrese un numero para poder calcular el area: ")

    area = float(area)
    area = 3.14 * area ** 2

    return area

area_calculada = calcular_area()
print("El area del circulo es de:", area_calculada)