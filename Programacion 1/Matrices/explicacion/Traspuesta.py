matriz =[
        [4,7,9],  
        [7,9,8], 
        [1,9,3],
        [4,3,7]]

M = len(matriz)       
N = len(matriz[0])

for j in range(N):           #Columnas
    for i in range(M):       #Filas
        print(f"{matriz[i][j]:5}", end = " ")
    print("")