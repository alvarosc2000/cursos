def merge_sorted_arrays(arr1, arr2):
    lista = []
    i, j = 0, 0  # índices para arr1 y arr2

    # Comparar y añadir el menor elemento de cada lista
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            lista.append(arr1[i])
            i += 1
        else:
            lista.append(arr2[j])
            j += 1

    # Añadir los elementos restantes de arr1 o arr2
    while i < len(arr1):
        lista.append(arr1[i])
        i += 1

    while j < len(arr2):
        lista.append(arr2[j])
        j += 1

    return lista

# Ejemplo para probar
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(merge_sorted_arrays(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6]
