def removeArrayPart(inputArray, l, r):
    nuevo = []
    for i in range(len(inputArray)):
        if i < l or i > r:
            nuevo.append(inputArray[i])

    return nuevo

# Prueba
print(removeArrayPart([1, 2, 3, 4, 5], 1, 3))  # [1, 5]
