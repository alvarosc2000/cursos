def suma_alternativa(cad1):
    array1 = []
    array2 = []
    for i in range(len(cad1)):
        if i % 2 == 0:
            array1.append(cad1[i])
        else:
            array2.append(cad1[i])
    
    return [sum(array1),sum(array2)]


print(suma_alternativa([50,60,60,45,70]))