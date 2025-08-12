def subconjunto_suma(nums, objetivo):
    for i in range(len(nums)):
        j = i + 1
        # Fijate que cerré el paréntesis de sum() antes de comparar con objetivo
        while j <= len(nums) and sum(nums[i:j]) < objetivo:
            j += 1
        # Igual aquí, cerramos sum() antes de comparar con objetivo
        if sum(nums[i:j]) == objetivo:
            return True
    # Si terminas el for sin encontrar, devuelves False aquí afuera
    return False


# Ejemplo para probar
print(subconjunto_suma([3, 34, 4, 12, 5, 2], 9))  # True
print(subconjunto_suma([1, 2, 3], 7))             # False
