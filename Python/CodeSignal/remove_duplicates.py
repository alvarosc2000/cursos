def remove_duplicates(nums):
    array_aux = []
    for i in range(len(nums)):
        if nums[i] not in array_aux:
            array_aux.append(nums[i])
    return array_aux

# Ejemplos:
arr1 = [1,1,2]
print(remove_duplicates(arr1))   # 2, arr1 modificado → [1,2]
arr2 = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicates(arr2))   # 5, arr2 modificado → [0,1,2,3,4]
