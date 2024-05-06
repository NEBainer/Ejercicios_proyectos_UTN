matriz = [[0]*3 for _ in range(4)]

M = len(matriz)       #Otra manera mas prolija
N = len(matriz[0])

for i in range(M):
    for j in range(N):
        print(f"{matriz[i][j]}", end= " ")
    print("")