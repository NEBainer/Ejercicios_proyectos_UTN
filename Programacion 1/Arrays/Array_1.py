'''1) Escribir una función que reciba una lista de enteros, la misma calculará y devolverá el promedio de todos los números.'''
def promedio_de_numeros(lista: list) -> float:
    sumatoria = 0
    for i in range(len(lista)):
        sumatoria += lista[i]

    promedio = sumatoria / len(lista)
    return promedio


mi_lista = [10,12,10,30]

lista_promediada = promedio_de_numeros(mi_lista)
print(f"El promedio de todos los numeros de la lista es: {lista_promediada}")