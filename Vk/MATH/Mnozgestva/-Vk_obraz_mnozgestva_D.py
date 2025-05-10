import math

def trueSQRT(n):
    i = float(math.sqrt(n))
    return -i,i

n = float(input())
print(*trueSQRT(n))