def palindromo(palindormo):
    for i in range(len(palindormo)):
        if (palindormo[i] != palindormo[-(i+1)]):
            return False
    return True


print(palindromo("aabaa"))