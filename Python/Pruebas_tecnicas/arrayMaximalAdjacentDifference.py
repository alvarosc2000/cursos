def arrayMaximalAdjacentDifference(inputArray):
    maxima_diferencia = 0
    for i in range(len(inputArray)-1):
        if abs(inputArray[i]-inputArray[i+1]) > maxima_diferencia:
            maxima_diferencia = abs(inputArray[i]-inputArray[i+1])
    return maxima_diferencia

# Prueba
print(arrayMaximalAdjacentDifference([2, 4, -11, 0]))  # 3
