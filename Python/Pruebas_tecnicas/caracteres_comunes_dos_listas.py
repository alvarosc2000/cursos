def caracteres_repetidos(cadena1,cadena2):
    lista_rep = ""
    total = 0
    for i in range(len(cadena1)):
        if cadena1[i] not in lista_rep and cadena1[i] in cadena2:
            veces_cadena1 = cadena1.count(cadena1[i])
            veces_cadena2 = cadena2.count(cadena1[i])    

            total += min(veces_cadena1,veces_cadena2)
            lista_rep += cadena1[i]

    return total

print(caracteres_repetidos("aabcc","adcaa"))