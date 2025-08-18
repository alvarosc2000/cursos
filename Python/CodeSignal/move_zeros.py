def move_zeros(nums):
    aux = []
    contador_ceros = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            aux.append(nums[i])
        else:
            contador_ceros += 1
    
    while(contador_ceros > 0):
            aux.append(0)
            contador_ceros -=1

    return aux

# Ejemplos:
print(move_zeros([0,1,0,3,12])) # [1,3,12,0,0]
print(move_zeros([0,0,1]))      # [1,0,0]
