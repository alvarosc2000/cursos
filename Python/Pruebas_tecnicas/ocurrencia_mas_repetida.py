def ocurrencias_mas(lista):
    maxima_ocurrencias = 0
    numero = None

    for i in range(len(lista)):
        if lista.count(lista[i]) > maxima_ocurrencias:
            maxima_ocurrencias = lista.count(lista[i])
            numero = lista[i]
    
    return numero


print(ocurrencias_mas([3,5,4,3,4,4,3,3]))