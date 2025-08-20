def sequence(cadena):
    errores = 0
    for i in range(len(cadena) - 1):
        if cadena[i] >= cadena[i + 1]:
            errores += 1
            if errores > 1:
                return False
            # Checamos si eliminar cadena[i] o cadena[i+1] arregla el problema
            if i > 0 and cadena[i - 1] >= cadena[i + 1]:
                if i + 2 < len(cadena) and cadena[i] >= cadena[i + 2]:
                    return False
    return True


print(sequence([1, 3, 2, 1]))  # False
print(sequence([1, 3, 2]))     # True
print(sequence([10, 1, 2, 3, 4, 5]))  # True
print(sequence([1, 2, 1, 2]))  # False
