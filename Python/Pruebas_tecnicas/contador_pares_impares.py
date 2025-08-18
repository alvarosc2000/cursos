def contadores(lista):
    contador_pares = 0
    contador_impares = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            contador_pares +=1
        else:
            contador_impares += 1
    
    return contador_pares, contador_impares

cp, ci = contadores([1, 2, 3, 4, 5])
print(f"Los numeros paren son: {cp}")
print(f"Los numeros impares son: {ci}")
