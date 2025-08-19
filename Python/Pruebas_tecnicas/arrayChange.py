def arrayChange(cadena):
    operaciones = 0
    for i in range(len(cadena)-1):
        if cadena[i+1] <= cadena[i]:
            diff = cadena[i] - cadena[i+1] + 1
            cadena[i+1] += diff
            operaciones += diff
    return operaciones

print(arrayChange([1, 1, 1]))  # 3
print(arrayChange([3, 2, 1]))  # 3
print(arrayChange([1, 2, 3]))  # 0
