def merge_sorted_arrays(arr1, arr2):
    new_array = arr1 + arr2  # Concatenar ambas listas
    return sorted(new_array)  # Ordenar la lista resultante

# Ejemplo para probar
print(merge_sorted_arrays([1, 3, 5], [2, 4, 6]))  # Output esperado: [1, 2, 3, 4, 5, 6]
print(merge_sorted_arrays([0, 10], [5, 7, 12]))   # Output esperado: [0, 5, 7, 10, 12]
