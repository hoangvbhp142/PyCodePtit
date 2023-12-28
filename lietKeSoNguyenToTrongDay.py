import math

def check(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True

n = input()
arr = [int(i) for i in input().split()]
dictt = {}
for i in arr:
    if check(i) == True:
        if i in dictt:
            dictt[i] += 1
        else:
            dictt[i] = 1
for i in dictt:
    print(f"{i} {dictt[i]}")