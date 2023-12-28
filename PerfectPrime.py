import math

def isPrime(a):
    if a == 2 or a == 3 or a == 5 or a == 7:
        return True
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a) + 1)):
        if a % i == 0:
            return False
    return True

def check(a):
    dao = int(a[::-1])
    sum = 0
    for i in a:
        if isPrime(int(i)) == False:
            return False
        sum += int(i)
    return isPrime(int(a)) and isPrime(dao) and isPrime(sum)
    

test = int(input())
while test != 0:
    test -= 1
    n = input()
    if check(n):
        print("Yes")
    else:
        print("No")
    
            

