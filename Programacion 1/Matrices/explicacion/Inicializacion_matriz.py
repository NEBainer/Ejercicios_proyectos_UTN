# rango M 4x3
matriz =[
        [4,7,9],  
        [7,9,8], 
        [1,9,3],
        [4,3,7]]  #Las matrices deben tener la misma cantidad de elementos por fila y la misma cantidad de columnas, o sino ya no es una matriz.

#Recorrer una matriz(De esta manera imprimimos las posiciones de la matriz, no el contenido del elemento)
for i in range(4):
    for j in range(3):
        print(f"{i}----{j}")

#Manera de devolver el valor de un elemento en una posicion determinada(Hardcodeando)
print(matriz[2][1])

#De esta manera podemos imprimir los valores que tiene la matriz en cada posicion.UTILLLL!!!!!
for i in range(len(matriz)):
    for j in range(len(matriz[0])): #Si en vez de cero aca ponemos "i" nos va a imprimir todo, inclusive si es una matriz media irregular, cosa que con el cero solo imprime una matriz cuadrada
        print(f"{matriz[i][j]}", end = " ") #Normalmente es como si tuviera un "\n" invisible. El "end =" lo elimina
    print("") #Agrega un salto de linea despues de imprimir todos los elementos de una misma fila