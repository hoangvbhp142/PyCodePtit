import math

def check(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True

test = int(input())
while test != 0:
    test -= 1
    n = input()
    dau, cuoi = n[0:3], n[len(n) - 3:]
    if check(int(dau)) == True and check(int(cuoi)) == True:
        print("YES")
    else:
        print("NO")