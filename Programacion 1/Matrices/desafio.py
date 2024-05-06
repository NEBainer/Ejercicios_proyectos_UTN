'''Desarrollar programa que sea capaz de multiplicar dos matrices ingresadas por el usuario. Validar las dimensiones de cada una para que sea consistente con el procedimiento

Alumnos: Doyel Alvarenga, Bainer Ezequiel y Morales Silva David

Link del video explicando: https://drive.google.com/drive/folders/14CmKRmFu68pGcX1-Dh1sEUuRa8_x8ymf?usp=drive_link '''

def multiplicar_matrices(matriz1, matriz2):
    filas_matriz1 = len(matriz1)
    columnas_matriz1 = len(matriz1[0])
    filas_matriz2 = len(matriz2)
    columnas_matriz2 = len(matriz2[0])

    # Verificar si las dimensiones son consistentes para la multiplicación
    if columnas_matriz1 != filas_matriz2:
        print("No se pueden multiplicar estas matrices. Las dimensiones no son consistentes.")
        return None

    # Crear matriz resultado inicializada con ceros
    resultado = [[0] * columnas_matriz2 for _ in range(filas_matriz1)]

    # Multiplicación de matrices
    for i in range(filas_matriz1):
        for j in range(columnas_matriz2):
            for k in range(filas_matriz2):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado

def ingresar_matriz():
    matriz = []
    filas = int(input("Ingrese el número de filas de la matriz: "))
    columnas = int(input("Ingrese el número de columnas de la matriz: "))

    print("Ingrese los elementos de la matriz fila por fila:")

    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = int(input(f"Ingrese el elemento [{i + 1}][{j + 1}]: "))
            fila += [elemento]
        matriz += [fila]

    return matriz

def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]:5}", end= " ")
        print("")

# Ingreso de las dos matrices
print("Ingrese la primera matriz:")
matriz1 = ingresar_matriz()

print("\nIngrese la segunda matriz:")
matriz2 = ingresar_matriz()


# Multiplicación de matrices y visualización del resultado
resultado = multiplicar_matrices(matriz1, matriz2)
if resultado:
    print("\nEl resultado de la multiplicación de las matrices es: ")
    imprimir_matriz(resultado)