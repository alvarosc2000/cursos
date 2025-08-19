def areSimilar(c1, c2):
    if len(c1) != len(c2):
        return False
    
    contador_1 = 0
    for i in range(len(c1)):
        if c1[i] != c2[i]:
            contador_1 += 1
    
    return contador_1 <= 2  # returns True if 2 or fewer differences

# Example usage
print(areSimilar([1, 2, 3, 4], [1, 2, 4, 3]))  # True
print(areSimilar([1, 2, 3, 4], [4, 3, 2, 1]))  # False
