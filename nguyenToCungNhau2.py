import math

n = int(input())
array = [int(number) for number in input().split()]
array.sort()
for i in range(0, n - 1):
    for j in range(i + 1, n):
        if math.gcd(array[i], array[j]) == 1:
            print(f"{array[i]} {array[j]}")