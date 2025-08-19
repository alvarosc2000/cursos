def sorting(cadena):
    cadena_pares = []
    cadena_impares = []
    cadena_final = []
    for i in range(len(cadena)):
        if cadena[i] % 2 == 0:
            cadena_pares.append(cadena[i])
        else:
            cadena_impares.append(cadena[i])
    
    cadena_final += sorted(cadena_pares)
    cadena_impares = sorted(cadena_impares)
    for j in range(len(cadena_impares)-1,-1,-1):
        cadena_final.append(cadena_impares[j])
    
    return cadena_final


print(sorting([5, 3, 2, 8, 1, 4]))