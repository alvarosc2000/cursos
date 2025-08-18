def remove_duplicates(nums):
    new_array = []
    for i in range (len(nums)):
        if nums[i] not in new_array:
            new_array.append(nums[i])
    
    return len(new_array)

# Ejemplos:
print(remove_duplicates([1,1,2]))        # 2
print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))  # 5
