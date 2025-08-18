def is_valid_parentheses(s):
    stack = []
    # Diccionario para mapear cierres a aperturas
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():
            # Si es apertura, la metemos en la pila
            stack.append(char)
        elif char in mapping:
            # Si es cierre, comprobamos que coincida con el tope de la pila
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            # Carácter inesperado (no paréntesis) - opcional según problema
            return False

    # Al final, la pila debe quedar vacía para que sea válido
    return len(stack) == 0

# Ejemplos para probar
print(is_valid_parentheses("()"))        # True
print(is_valid_parentheses("()[]{}"))    # True
print(is_valid_parentheses("(]"))        # False
print(is_valid_parentheses("([)]"))      # False
print(is_valid_parentheses("{[]}"))      # True
