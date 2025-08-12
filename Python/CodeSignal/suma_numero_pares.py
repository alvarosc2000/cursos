def sum_even_numbers(numbers):
    suma = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            suma += numbers[i]

    return suma
# Ejemplo para probar
print(sum_even_numbers([1, 2, 3, 4, 5]))  # Output esperado: 6
print(sum_even_numbers([10, 11, 12]))     # Output esperado: 22
