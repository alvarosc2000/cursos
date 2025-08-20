def reverseInParentheses(s):
    stack = []
    
    for char in s:
        if char == ")":
            temp = []
            # sacar hasta '('
            while stack and stack[-1] != "(":
                temp.append(stack.pop())
            stack.pop()  # quitar '('
            # volver a meter invertido
            stack.extend(temp)
        else:
            stack.append(char)
    
    return "".join(stack)


# Ejemplos
print(reverseInParentheses("(bar)"))          # "rab"
print(reverseInParentheses("foo(bar)baz"))    # "foorabbaz"
print(reverseInParentheses("foo(bar(baz))"))  # "foobazrab"
