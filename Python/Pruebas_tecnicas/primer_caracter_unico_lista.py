def first_unique_char(s):
    # Contar cuántas veces aparece cada carácter
    counts = []
    for i in range(len(s)):
        count = 0
        for j in range(len(s)):
            if s[i] == s[j]:
                count += 1
        counts.append(count)
    
    # Buscar el primer índice con count == 1
    for i in range(len(counts)):
        if counts[i] == 1:
            return i
    return -1

# Ejemplos:
print(first_unique_char("leetcode"))     # 0
print(first_unique_char("loveleetcode")) # 2
print(first_unique_char("aabb"))         # -1
