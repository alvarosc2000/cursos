def interseccion_ordenada(A, B):
    lista = []
    for i in range(len(A)):
        if A[i] not in lista and A[i] in B:
            lista.append(A[i])

    return lista

# Pruebas rápidas
print(interseccion_ordenada([1, 2, 2, 3], [2, 2, 4]))  # [2]
