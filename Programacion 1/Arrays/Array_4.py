'''4)Escribir una función que reciba como parámetros una lista de enteros y retorne la posición del valor máximo encontrado.'''
def encontrar_valor_maximo(lista: list) -> int:
    bandera = True
    for i in range(len(lista)):
        if bandera == True or lista[i] > valor_maximo:
            valor_maximo = lista[i]
            posicion_maxima = i+1
            bandera = False
        
    return posicion_maxima

mi_lista = [5,3,10,8]

lista_con_maximo = encontrar_valor_maximo(mi_lista)
print(f"El valor maximo encontrado en la lista esta en la posicion: {lista_con_maximo}")