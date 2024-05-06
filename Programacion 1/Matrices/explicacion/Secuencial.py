matriz = [[0]*3 for _ in range(4)]

M = len(matriz)       
N = len(matriz[0])

for i in range(M):    #Manera para ir cargando los numeros en una matriz
    for j in range(N):
        matriz[i][j] = int(input("Ingrese un numero: "))



for i in range(M):
    for j in range(N):
        print(f"{matriz[i][j]:5}", end= " ")   #El ":5" establece la cantidad de caracteres de espacio que habra entre elemento de la matriz 
    print("")