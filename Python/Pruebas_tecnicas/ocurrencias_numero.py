def ocurrencias_numero(lista):
    mostrados = []
    for i in range(len(lista)):
        if lista[i] not in mostrados:
            print(lista[i], lista.count(lista[i]))
            mostrados.append(lista[i])


(ocurrencias_numero([1,2,2,3,4,3,4,7,5,3]))