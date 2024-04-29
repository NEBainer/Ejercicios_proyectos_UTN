'''2)Escribir una función parecida a la anterior, pero la misma deberá calcular y devolver el promedio de los números positivos.'''
def promedio_de_numeros(lista: list) -> float:
    sumatoria = 0
    contador_positivos = 0
    for i in range(len(lista)):
        if lista[i] > 0:
            contador_positivos += 1
            sumatoria += lista[i]

    promedio = sumatoria / contador_positivos

    return promedio

mi_lista = [10,-32,3,-2,-14,2]

lista_promediada = promedio_de_numeros(mi_lista)
print(f"El promedio de todos los numeros de la lista es: {lista_promediada}")