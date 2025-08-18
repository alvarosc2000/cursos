import math


def centuryFromYear(year):
    return math.ceil(year/100)



print(centuryFromYear(1905))
print(centuryFromYear(1700))
