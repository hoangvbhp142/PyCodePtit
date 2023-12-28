import math

def UCLN(a, b):
    if a == 1 or b == 1:
        return 1
    while(a != b):
        if a > b:
            a -= b
        else:
            b -= a
    return a

def snt(a):
    if a < 2:
        return False
    for i in range(2,int(math.sqrt(a))+1):
        if a % i == 0:
            return False
    return True


test = int(input())
while test != 0:
    test -= 1
    n = int(input())
    dem = 0
    for i in range(1, n):
        if UCLN(n,i) == 1:
            dem += 1
    if snt(dem) == True:
        print("YES")
    else:
        print("NO")

