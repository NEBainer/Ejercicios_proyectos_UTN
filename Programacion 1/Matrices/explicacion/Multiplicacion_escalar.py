matriz =[
        [4,7,9],  
        [7,9,8], 
        [1,9,3],
        [4,3,7]]

escalar = 5

matriz_producto = [[0] * len(matriz[0]) for _ in range(len(matriz))]

for i in range(len(matriz_producto)):
    for j in range(len(matriz_producto[0])):
        matriz_producto[i][j] = matriz[i][j] * escalar

for i in range(len(matriz_producto)):
    for j in range(len(matriz_producto[i])):
        print(f"{matriz_producto[i][j]:5}", end = " ")
    print("")