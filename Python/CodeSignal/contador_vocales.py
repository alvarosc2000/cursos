def count_vowels(s):
    contador = 0
    vocales = {'a','e','i','o','u'}

    s = ''.join(c.lower() for c in s if c.isalnum())

    for i in range(len(s)):
        if s[i] in vocales:
            contador += 1
    return contador

# Ejemplos:
print(count_vowels("hello world"))   # 3
print(count_vowels("AEIOU aeiou"))   # 10
print(count_vowels("Python"))        # 1
