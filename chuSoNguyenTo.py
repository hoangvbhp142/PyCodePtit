import math

def isPrime(a):
    if a < 2:
        return False
    if a == 2 or a == 3 or a == 5 or a == 7:
        return True
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True

def check(a):
    prime = 0
    notprime = 0
    for i in a:
        if isPrime(int(i)):
            prime += 1
        else:
            notprime += 1
    if prime > notprime and isPrime(len(a)) == True:
        return True
    return False

t = int(input())
while t != 0:
    t -= 1
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")