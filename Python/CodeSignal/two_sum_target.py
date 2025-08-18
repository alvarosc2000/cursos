def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)-1,-1,-1):
            if j != i and nums[i]+nums[j] == target:
                return [i,j]
    return None

# Ejemplos para probar
print(two_sum([2, 3, 7, 15], 9))  # Output esperado: [0, 1]
print(two_sum([3, 2, 4], 6))       # Output esperado: [1, 2]
print(two_sum([3, 3], 6))          # Output esperado: [0, 1]
