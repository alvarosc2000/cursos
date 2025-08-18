def eliminar_duplicados(lista):
    aux = []
    for i in range(len(lista)):
        if(lista[i] not in aux):
            aux.append(lista[i])
    
    return aux

print(eliminar_duplicados([1,3,2,3,2]))