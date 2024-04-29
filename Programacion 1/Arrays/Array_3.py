'''3)Escribir una función que calcule y retorne el producto de todos los elementos de la lista que recibe como parámetro.'''
def producto_de_numeros(lista: list) -> int:
    acumulador = 1
    for i in range(len(lista)):
        acumulador = lista[i] * acumulador

    return acumulador

mi_lista = [2,1,4,2]

lista_multiplicada = producto_de_numeros(mi_lista)
print(f"El producto de todos los elementos de la lista es: {lista_multiplicada}")