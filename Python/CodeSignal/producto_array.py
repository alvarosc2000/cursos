def productos_sin_yo(nums):
    n = len(nums)
    
    # Paso 1: productos antes de i
    new_array = []
    prod = 1
    for i in range(n):
        new_array.append(prod)
        prod *= nums[i]
    
    # Paso 2: productos después de i
    prod = 1
    for i in range(n - 1, -1, -1):
        new_array[i] *= prod
        prod *= nums[i]
    
    return new_array


# Prueba rápida
print(productos_sin_yo([1, 2, 3, 4]))  # [24, 12, 8, 6]
