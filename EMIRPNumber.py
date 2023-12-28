import math

def doixung(s):
    dao = str(s)[::-1]
    if int(dao) == s:
        return -1
    return int(dao)

def nguyento(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True

test = int(input())
while test != 0:
    test -= 1
    n = int(input())
    check = [0] * n
    for i in range(13, n + 1):
        if nguyento(i) == True and doixung(i) != -1:
            if doixung(i) <= n and nguyento(doixung(i)) == True:
                if check[i] == 0 and check[doixung(i)] == 0:
                    print(f"{i} {doixung(i)}", end = " ")
                    check[i] = check[doixung(i)] = 1
    print()


