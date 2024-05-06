matriz =[
        [4,7,9],  
        [7,9,8], 
        [1,9,3],
        [4,3,7]]

matriz_b = [
    [4,3,6],
    [12,2,-1],
    [-3,4,9],
    [14,-21,1]
]

matriz_suma = [[0] * len(matriz[0]) for _ in range(len(matriz))]

for i in range(len(matriz_suma)):
    for j in range(len(matriz_suma[0])):
        matriz_suma[i][j] = matriz[i][j] + matriz_b[i][j]

for i in range(len(matriz_suma)):
    for j in range(len(matriz_suma[i])):
        print(f"{matriz_suma[i][j]:5}", end = " ")
    print("")