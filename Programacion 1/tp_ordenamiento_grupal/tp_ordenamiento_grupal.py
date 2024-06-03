import time

lista = [1,6,5,3]

#\\\\\\\\\\ ordenamiento por quicksort
# for i in range(0, len(lista) - 1):
#     print(f'{i}\n')
#     for j in range(i + 1, len(lista)):
#         print(f'\t{j}')
# start = time.time()
# for i in range(0, len(lista) - 1):
#     for j in range(i + 1, len(lista)):
#         print(lista[i], lista[j])
#         if lista[i] > lista[j]:
#             print('entra al condicional')
#             ## SWAP 
#             ##salvo valor de i
#             auxiliar = lista[i]
#             ##lo rescribo con el nro mayor
#             lista[i] = lista [j]
#             #reemplazo 
#             lista[j] = auxiliar
#             print(lista[i], lista[j], 'reemplaza')
#     print(lista)

# print(lista)
# end = time.time()

# print(end - start)

lista_dos = [4, 3, 5, 1 ,2]
def bubble_sort(lista):
    n = len(lista)
    for i in range(0,n - 1):
        print('i',lista[i])
        for j in range(n - 1):
            print(lista, 'lista antes')
            print(f'j:{j} valor: {lista[j]}')    
            if lista[j] > lista[j + 1] :
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print('j:',lista[j], 'j+1', lista[j+1], 'cambiado')
                print(lista, 'lista dps')
    
vector = [3, 8, 1, 4, 7]
bubble_sort(lista_dos)

'''2) y 3)'''
# Definimos la lista desordenada del video
lista = [4, 3, 5, 1, 2]

# Definimos la funcion bubble_sort que toma la "lista"
def bubble_sort(lista):
    # Obtiene el largo de la lista
    n = len(lista)
    
    # Itera desde el primer hasta el penúltimo elemento
    for i in range(n - 1):
        # Itera desde el primer elemento hasta el último elemento no ordenado
        for j in range(n - i - 1):
            # Compara elementos que estan unos al lado de otros.
            if lista[j] > lista[j + 1]:
                # Intercambia elementos si están en el orden incorrecto
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Nueva lista a ordenar (No afecta en nada a la lista anterior)
vector = [3, 8, 1, 4, 7]

# Llama a la función bubble_sort para ordenar la lista "lista"
bubble_sort(lista)

# Imprime la lista ordenada
for i in range(len(lista)):
    print(lista[i], end= " ")  # Lo que se espera que muestre en consola: [1, 2, 3, 4, 5]

'''PARTE 1'''
c = 0  # Contador global para rastrear el número de llamadas recursivas

def swap(a: int, b: int):
    return b, a  # Intercambia los valores de a y b

def particionar(array, low, high):
    pivote = array[high]  # El pivote es el último elemento de la lista
    i = low - 1  # Inicializa el índice de los elementos menores al pivote
        
    for j in range(low, high):
        if array[j] <= pivote:  # Si el elemento actual es menor o igual al pivote
            i += 1
            array[i], array[j] = swap(array[i], array[j])  # Intercambia elementos
    
    array[i + 1], array[high] = swap(array[i + 1], array[high])  # Coloca el pivote en su posición correcta
    
    return i + 1  # Devuelve la posición del pivote

def quick_sort(array, low, high):
    global c
    c += 1  # Incrementa el contador de llamadas recursivas
    if low < high:
        pi = particionar(array, low, high)  # Particiona el array y obtiene la posición del pivote
        quick_sort(array, low, pi - 1)  # Ordena recursivamente la sublista izquierda
        quick_sort(array, pi + 1, high)  # Ordena recursivamente la sublista derecha

import time

vector = [5,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,1,9,7,3,1,9,7,3,1,9,7,
          3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
          1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
          1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
          1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
          1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
          1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3]
start = time.time()
quick_sort(vector, 0 , len(vector) - 1)
end = time.time()

print(f"Tiempo: {(end - start)*1000} ms")  # Imprime el tiempo de ejecución en milisegundos
print(c)  # Imprime el número de llamadas recursivas
print(len(vector))  # Imprime la longitud del vector
print(vector)  # Imprime el vector ordenado

#Forma de implementar el algoritmo QuickSort sin usar recursión
def iterativo_quick_sort(array):
    global c
    c = 0  # Reinicia el contador global
    stack = [(0, len(array) - 1)]  # Inicializa la pila con el rango completo del array

    while stack:
        low, high = stack.pop()  # Desapila el siguiente rango a procesar
        if low < high:
            pi = particionar(array, low, high)  # Particiona el array y obtiene la posición del pivote
            stack.append((low, pi - 1))  # Apila el rango izquierdo
            stack.append((pi + 1, high))  # Apila el rango derecho
            c += 1  # Incrementa el contador de iteraciones

import time

vector = [5,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,1,9,7,3,1,9,7,3,1,9,7,
3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3]

start = time.time()
iterativo_quick_sort(vector)
end = time.time()

print(f"Tiempo: {(end - start)*1000} ms")  # Imprime el tiempo de ejecución en milisegundos
print(c)  # Imprime el número de iteraciones
print(len(vector))  # Imprime la longitud del vector
print(vector)  # Imprime el vector ordenado

'''Diferencias en Performance
Uso de memoria: La versión recursiva utiliza el stack de llamadas del sistema, lo que puede llevar a un stack overflow si el array es muy grande. La versión iterativa, por otro lado, utiliza una pila explícita en la memoria heap, lo que es más seguro para grandes tamaños de entrada.

Velocidad: En términos de velocidad pura, ambas versiones deberían ser comparables en la mayoría de los casos, pero la implementación iterativa puede ser un poco más lenta debido a la sobrecarga de manejo de la pila explícita.

Legibilidad y mantenimiento: La versión recursiva es más fácil de entender y seguir, lo que puede hacerla más adecuada para aplicaciones donde la claridad del código es importante.

Al final, la elección entre recursiva e iterativa dependerá del contexto específico y las limitaciones del entorno donde se va a ejecutar el código.'''

'''PARTE 2'''
'''2) y 3)'''
# Definimos la lista desordenada del video
lista = [4, 3, 5, 1, 2]

# Definimos la funcion bubble_sort que toma la "lista"
def bubble_sort(lista):
    # Obtiene el largo de la lista
    n = len(lista)
    
    # Itera desde el primer hasta el penúltimo elemento
    for i in range(n - 1):
        # Itera desde el primer elemento hasta el último elemento no ordenado
        for j in range(n - i - 1):
            # Compara elementos que estan unos al lado de otros.
            if lista[j] > lista[j + 1]:
                # Intercambia elementos si están en el orden incorrecto
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Nueva lista a ordenar (No afecta en nada a la lista anterior)
vector = [3, 8, 1, 4, 7]

# Llama a la función bubble_sort para ordenar la lista "lista"
bubble_sort(lista)
# Imprime la lista ordenada
for i in range(len(lista)):
    print(lista[i], end= " ")  # Lo que se espera que muestre en consola: [1, 2, 3, 4, 5]

'''4) Algoritmo de Ordenamiento por Burbuja (Bubble Sort)
Descripción:
El algoritmo de burbuja compara cada par de elementos que estan unos al lado de otros y los intercambia si están en el orden incorrecto. 
Este proceso se repite varias veces hasta que la lista esté ordenada. El burbujeo es Fácil de entender e implementar. 
Sus ventajas son que es simple y efectivo para listas pequeñas y sus desventajas, que es muy ineficiente para listas grandes.

Codigo:
def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

Algoritmo de Ordenamiento por Selección (Selection Sort)
Descripción:
El algoritmo de selección encuentra el elemento más pequeño de la lista y lo coloca en la primera posición.
Luego encuentra el siguiente más pequeño y lo coloca en la segunda posición, y así sucesivamente. 
Tambien es fácil de entender e implementar. Sus ventajas son que realiza menos intercambios que el burbujeo y sus desventajas son que es muy ineficiente para listas grandes y no mejora con listas casi ordenadas.

Codigo:
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_indice = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_indice]:
                min_indice = j
        lista[i], lista[min_indice] = lista[min_indice], lista[i]
'''
'''5) Ventajas de nuestro algoritmo de burbuja:
-Fácil de Entender e Implementar: La lógica detrás del algoritmo de burbujeo es sencilla. Compara elementos que estan unos al lado de otros y los intercambia si están en el orden incorrecto, repitiendo este proceso hasta que la lista esté ordenada.
Es ideal para enseñar y aprender los conceptos básicos de algoritmos de ordenamiento.

-No cambia el orden relativo de los elementos con valores iguales. Esto es importante si la estabilidad es una consideración necesaria para el problema.

Desventajas de nuestro algoritmo
-Es ineficiente para Listas Grandes debido a su complejidad de tiempo, no es adecuado para listas de gran tamaño.

-Número de Comparaciones: En el peor caso, realiza un número muy elevado de comparaciones, ya que cada par de elementos se compara repetidamente.

Complejidad en el Peor Caso:
Peor Caso: Cuando la lista está en orden inverso, cada elemento debe ser comparado con todos los demás.
Caso Promedio: Incluso en listas aleatoriamente ordenadas, el algoritmo de burbuja no mejora significativamente en comparación con su peor caso.
Mejor Caso: Si la lista ya está ordenada, solo requiere una pasada para verificar que no se necesitan más intercambios. Sin embargo, esta situación es poco frecuente en aplicaciones prácticas.

En el peor caso (lista en orden inverso), el número de comparaciones es O(n²). Por ejemplo, para una lista de tamaño 5, se realizarán 10 comparaciones en la primera pasada, 9 en la segunda, y así sucesivamente, totalizando 10 + 9 + 8 + 7 + 6 = 40 comparaciones.
Intercambios:

También en el peor caso, cada comparación desfavorable resulta en un intercambio. Así, el número de intercambios también es O(n²).'''

'''
6) A lo largo de este trabajo practico hemos logrado trabjar y comparar los algoritmos de bubujeo, de selección y 'QuickSort'. Cada uno de estos presenta ventajas y desventajas por lo cual 
es necesario analizar cual se adecua a nuestras necesidades.

Para una lista de 1022 elementos ordenados de manera aleatoria, el metodo de burbujeo realiza 1043462 comparaciones para llegar 
al resultado final, intercambia entre sí 257267 números y tarda aproximadamente 0.075 ms. 
El metodod de seleccion realiza 521731 comparaciones, intercambia posiciones 18160 y tarda 0.025 ms .
El 'Quicksort' realiza 10783 comparaciones, intercambia 6253 veces y tarda 0.002 ms.

Para una lista de 144 elementos el método 'quicksort' realiza 930 comparaciones y hace 436 swaps en un tiempo de  ~ 0 s.
El método de burbujeo realiza 20592 comparaciones y hace 5297 swaps en un tiempo de 0.001 ms
El método de selección, por su parte, realiza 10296 comparaciones y 1932 swaps en ~0 segundos.

Para una lista de 30 elementos 'Quicksort' realiza 122 comparaciones y 54 swaps. 
el método de burbujeo realiza 870 comparaciones y 207 swaps.
el método de selección 435 comparaciones y 170 swaps.
Los 3 metodos ordenaron la lista en 0 segundos.

Para una lista de 10 elementos quicksort compara 24 veces y hace 13 swaps
Burbujeo 90 comparaciones y 10 swaps
Selección 45 comparaciones 11 swaps

Conclusiones: luego de llevar acabo este trabajo práctico y este mini-experimento práctico podemos concluir que el algoritmo quicksort es el mas eficiente de estos tres. Realiza menor cantidad de comparaciones y swaps y en menos tiempo. Su desventaja pasa por el hecho
de que utiliza recursion por lo cual consume mas recursos. Esto puede ser corregido utilizando un bucle para reemplazar la recursión.
Por otro lado el metodo de burbujeo y de selección presentan una eficiencia parecida para listas cortas pero cuando las listas se hacen mas grandes el metodo de seleccion le saca una ventaja considerable.
'''




