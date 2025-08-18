def sumaParesConsecutivos(cadena):
    sumaMax = 0
    pares = []
    for i in range(len(cadena)-1):
        if sumaMax < cadena[i]*cadena[i+1]:
            sumaMax = cadena[i]*cadena[i+1]
            pares = [cadena[i],cadena[i+1]]
    
    return sumaMax, pares

suma, pares = sumaParesConsecutivos([3, 6, -2, -5, 7, 3])
print(f"La suma maxima es ---> {suma}")
print(f"los pares son {pares}")