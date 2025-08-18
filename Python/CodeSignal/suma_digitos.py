def sum_of_digits(n):
    suma = 0
    for digit in str(n):
        suma += int(digit)

    return suma

# Ejemplos:
print(sum_of_digits(123))  # 6
print(sum_of_digits(987))  # 24
