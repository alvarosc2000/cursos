def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    return (max(yourLeft, yourRight) == max(friendsLeft, friendsRight) and
            min(yourLeft, yourRight) == min(friendsLeft, friendsRight))

print(areEquallyStrong(10, 15, 15, 10))  # True
print(areEquallyStrong(10, 15, 10, 15))  # True
print(areEquallyStrong(10, 15, 10, 14))  # False
