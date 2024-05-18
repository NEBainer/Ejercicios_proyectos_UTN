# lista = [6, 5, 2, 7, 4, 1, 0, 3]
# '''Mecanica para ir moviendome en el burbujeo'''
# # for i in range(0, len(lista)-1):
# #     print(f"{i}\n")
# #     for j in range(i + 1, len(lista)):
# #         print(f"\t{j}")


# for i in range(0, len(lista)-1):
#     for j in range(i + 1, len(lista)):
#         if lista[i] > lista[j]:
#             auxiliar = lista[i]  # Rescato i en la variable auxiliar
#             lista[i] = lista[j]  # Como i la guarde en la auxiliar ahora puedo pisar su valor con lista j, ahora lista i valdrá lo que lista j
#             lista[j] = auxiliar  # Ahora lista j valdrá lo que valía lista i

# print(lista) #Ahora la lista estará ordenada

# #Intercambio de valores(Concepto de SWAP)
# a = 10
# b = 5

# c = a
# a = b
# b = c

# # a, b = b, a

# print(a)
# print(b)
nombres = ["Pepe", "Moni", "Ana", "Coqui"]

for i in range (0, len(nombres) - 1):
    for j in range(i + 1, len(nombres)):
        if nombres[i] > nombres[j]:
            auxiliar = nombres[i]
            nombres[i] = nombres[j] 
            nombres[j] = auxiliar
print(nombres)
