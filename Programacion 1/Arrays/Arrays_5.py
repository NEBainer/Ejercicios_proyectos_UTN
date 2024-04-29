'''5)Escribir una función que reciba como parámetros una lista de enteros y muestre la/las posiciones en donde se encuentra el valor máximo hallado.'''
def encontrar_valor_maximo(lista: list) -> list:
    bandera = True
    lista_maximos = [0] * len(lista) 
    contador_maximos = 0
    for i in range(len(lista)):
        if bandera == True or lista[i] > valor_maximo:
            valor_maximo = lista[i]
            lista_maximos[i] = i + 1  
            contador_maximos = 1  
            bandera = False
        elif lista[i] == valor_maximo:
            contador_maximos += 1  
            if contador_maximos > 1:
                lista_maximos[i] = i + 1  
    for i in range(len(lista_maximos)):
        if lista_maximos[i] != 0:
            print(lista_maximos[i], end = " ")

mi_lista = [10, 9, 10, 10]

print("El valor máximo encontrado en la lista está en la/las posiciones: ")
encontrar_valor_maximo(mi_lista)