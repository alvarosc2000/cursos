def caracteres_comunes(s1,s2):
    cadena = []
    for i in range(len(s1)):
        if s1[i] not in cadena and s1[i] in s2:
            cadena.append(s1[i])
    
    return cadena


print(caracteres_comunes([1,2,3,3],[3,4,4,5]))