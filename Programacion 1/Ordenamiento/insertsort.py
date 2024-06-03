''' ORDENAR UNA LISTA DE MAYOR A MENOR '''
'''  ALGORITMO INSERT '''

lista = [6, 5, 2, 7, 4, 1, 0, 3]        # 8 ELEMENTOS -> 7 ... 0 (8)

# Tomando la longitud, se restan '-1'(asegurando que comienze en el ultimo) | '-1' limite del bucle | -1 es el paso del rango

for i in range(len(lista) -1, -1, -1):  

    contadaor_pasos = 0
    for j in range(len(lista)-1, i, -1):
        contadaor_pasos += 1
        if lista[i] < lista[j]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

            print(f"{lista} paso {contadaor_pasos}")



