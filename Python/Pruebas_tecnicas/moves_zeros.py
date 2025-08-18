def moves(cadena):
    contador_ceros = 0
    aux = []
    for i in range(len(cadena)):
        if cadena[i] == 0:
            contador_ceros += 1
        else:
            aux.append(cadena[i])
    
    while(contador_ceros > 0):
        aux.append(0)
        contador_ceros -= 1
    
    return aux


print(moves([1,2,0,0,2,3]))