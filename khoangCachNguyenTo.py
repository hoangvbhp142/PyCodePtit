import math

def check(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True

def prime():
    primes = [0]
    i = 2
    while len(primes) < 1005:
        if check(i) == True:
            primes.append(i)
        i += 1
    return primes

nhap = [int(number) for number in input().split()]
n, x = nhap
primes = prime()
for i in range(0 , n + 1):
    print(x + primes[i], end = " ")
    x += primes[i]