def interseccion_ordenada(A, B):
    lista = []
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] in B and A[i] not in lista:
                        lista.append(A[i])
    

    return lista

# Pruebas rápidas
print(interseccion_ordenada([1, 2, 2, 3], [2, 2, 4]))  # [2]
