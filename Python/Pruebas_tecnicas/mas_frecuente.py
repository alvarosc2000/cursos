def masFrecuente(lista):
    mas_frecuente =  None
    for i in range(len(lista)-1):
        if lista.count(lista[i]) >= lista.count(lista[i+1]):
            mas_frecuente = lista[i]
    return mas_frecuente


print(masFrecuente([1,1,2,2]))