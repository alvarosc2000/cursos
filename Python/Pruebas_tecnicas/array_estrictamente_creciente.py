def estrictamente_creciente(lista):
    errores = 0
    for i in range(len(lista)-1):
        if lista[i] >= lista[i+1]:
            errores += 1
            if errores > 1:
                return False
    return True

print(estrictamente_creciente([1, 3, 2, 1]))  # False
print(estrictamente_creciente([1, 3, 2, 4]))  # True
