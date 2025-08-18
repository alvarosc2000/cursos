def arrayConsecutivo(lista):
    listaOrdenada = sorted(lista)
    valores_faltantes = 0
    for i in range(len(listaOrdenada)-1):
        if listaOrdenada[i+1] - listaOrdenada[i] > 1:
            valores_faltantes += listaOrdenada[i+1] - listaOrdenada[i]-1
    
    return (valores_faltantes)

print(arrayConsecutivo([6, 2, 3, 8]))