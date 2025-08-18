def elementos_unicos(lista):
    lista_aux = []
    for i in range(len(lista)):
        if lista[i] not in lista_aux and lista.count(lista[i]) == 1:
            lista_aux.append(lista[i])
    
    return lista_aux

print(elementos_unicos([1,2,3,4,3,4,5,6,7,4]))