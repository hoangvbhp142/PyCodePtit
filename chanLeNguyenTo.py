import math


def prime(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True


def check(n):
    summ = 0
    for i in range(len(n)):
        if i % 2 == 0 and int(n[i]) % 2 == 1:
            return False
        if i % 2 == 1 and int(n[i]) % 2 == 0:
            return False
        summ += int(n[i])
    if prime(summ):
        return True
    return False


test = int(input())
while test != 0:
    test -= 1
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")
