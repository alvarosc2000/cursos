def sumOfTwo(cadena1, cadena2, target):
    for i in range(len(cadena1)):
        for j in range(len(cadena2)):
            if cadena1[i] + cadena2[j] == target:
                return True
    return False

print(sumOfTwo([1, 2, 3], [10, 20, 30], 13))