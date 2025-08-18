def length_of_longest_substring(s):
    start = 0
    max_length = 0
    current_chars = []

    for char in s:
        if char in current_chars:
            # Quitar desde el inicio hasta la primera aparición del char repetido
            while current_chars[0] != char:
                current_chars.pop(0)
                start += 1
            current_chars.pop(0)
            start += 1
        current_chars.append(char)
        max_length = max(max_length, len(current_chars))

    return max_length

# Ejemplos para probar
print(length_of_longest_substring("abcabcbb"))  # Output esperado: 3
print(length_of_longest_substring("bbbbb"))     # Output esperado: 1
print(length_of_longest_substring("pwwkew"))    # Output esperado: 3
