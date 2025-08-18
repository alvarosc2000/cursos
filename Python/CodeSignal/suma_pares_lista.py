def sum_even_numbers(nums):
    suma = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            suma += nums[i]
    return suma

# Ejemplos:
print(sum_even_numbers([1,2,3,4,5]))    # 6
print(sum_even_numbers([2,4,6,8]))      # 20
print(sum_even_numbers([1,3,5]))        # 0
