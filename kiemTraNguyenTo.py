import math
def prime(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a  % i == 0:
            return False
    return True

t = int(input())
while t != 0:
    t -= 1
    n = input()
    num = int(n[len(n) - 4:])
    if prime(num):
        print("YES")
    else:
        print("NO")