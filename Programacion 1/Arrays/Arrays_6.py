'''6) Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista de nombres, un nombre a reemplazar y su correspondiente reemplazo. La función debe reemplazar cada ocurrencia del nombre a reemplazar en la lista con su correspondiente reemplazo y luego retornar la cantidad total de reemplazos realizados.'''
def reemplazar_nombres(lista: list, nombre: str, reemplazo: str) -> list|int:
    contador_reemplazos = 0
    for i in range(len(lista)):
        if lista[i] == nombre:
            lista[i] = reemplazo
            contador_reemplazos += 1
    return contador_reemplazos

mi_lista = ["Ezequiel", "Jony", "Jony", "Jony"]
lista_reemplazada = reemplazar_nombres(mi_lista, "Jony", "Doyel")

print(f"La cantidad de reemplazos realizados fueron: {lista_reemplazada}")
print(f"La lista actualizada: {mi_lista}")