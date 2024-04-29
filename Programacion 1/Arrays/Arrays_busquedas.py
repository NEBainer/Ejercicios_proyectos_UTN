lista = [1,5,-12,-13,9]

#contador = 0 Conviene mas hacerlo con bandera, es mas eficiente y gasto menos recursos, capaz el contador lo vamos a utilizar si tengo que contar la cantidad de negativos
bandera = False
for i in range(len(lista)):
    if lista[i] < 0:
        #contador += 1
        bandera = True
        break

#if contador > 0:
if bandera == True:
    print("Por lo menos hay un negativo")
else:
    print("No hay negativos")