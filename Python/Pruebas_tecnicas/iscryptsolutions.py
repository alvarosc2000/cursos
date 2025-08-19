def isCryptSolution(crypt, solution):
    nums = []
    
    for word in crypt:
        num = ""
        for c in word:
            for pair in solution:
                if pair[0] == c:
                    num += pair[1]
        # Revisar si tiene cero a la izquierda
        if len(num) > 1 and num[0] == '0':
            return False
        nums.append(int(num))
    
    return nums[0] + nums[1] == nums[2]

# Prueba
crypt = ["SEND", "MORE", "MONEY"]
solution = [['O', '0'], ['M', '1'], ['Y', '2'], ['E', '5'], ['N', '6'], ['D', '7'], ['R', '8'], ['S', '9']]
print(isCryptSolution(crypt, solution))  # True
