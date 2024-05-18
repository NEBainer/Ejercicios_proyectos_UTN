vector = [3,8,1,4,7]

for i in range(0, len(vector)-1): #El rango de iniciacion estaba mal, lo cambia a cero para que empiece desde el principio de los elementos del vector y al final le reste uno para que no se vaya de rango
    for j in range(i + 1, len(vector)): #Le sume 1 a i para que itere uno adelante y de esa manera va comprobando los numeros con el anterior, de tal manera que puede ir pisandolo si i es mas chico que j
        if vector[i] < vector[j]: #Antes era == y poniendo < podemos ordenarlo de manera descendente
            auxiliar = vector[i]
            vector[i] = vector[j] #En el caso de que se cumpla el condicional hago que [j] sea [i]
            vector[j] = auxiliar

for i in range(len(vector)):
    print(vector[i], end= " ")
