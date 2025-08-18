def contador(cadena):
    aux = ""
    for i in range(len(cadena)):
        if cadena[i] not in aux and cadena[i] != " " and cadena.count(cadena[i]) == 1:
            aux += cadena[i]
    
    return len(aux)


print(contador("Hola mundo"))
