def makeArrayConsecutive2(status):
    faltantes = 0
    status.sort()
    for i in range(0,len(status)-1):
        if (status[i+1]-status[i] > 1):
            faltantes += status[i+1] -status[i] -1
    
    return faltantes

print(makeArrayConsecutive2([6,2,3,8]))