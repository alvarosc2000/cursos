def contador_caracteres_unicos(cadena):
    apariciones = 0
    cadena_aux = ""
    for i in range(len(cadena)):
        if cadena.count(cadena[i]) == 1 and cadena[i] not in cadena_aux:
            apariciones +=1
            cadena_aux += cadena[i]
    
    return apariciones, cadena_aux

apariciones, letras = contador_caracteres_unicos("hello")
print(f"Hay {apariciones} en la {letras}")