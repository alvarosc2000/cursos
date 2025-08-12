def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    for i in range(0, len(s)//2):
        if s[i] != s[-(i+1)]:
            return False
    return True

# Ejemplo para probar
print(is_palindrome("A man, a plan, a canal, Panama!"))  # Output esperado: True
print(is_palindrome("Hello"))                            # Output esperado: False
