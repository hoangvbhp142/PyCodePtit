import math

nhap = input().split()
nhap = [int(number) for number in nhap]
n, k = nhap
cnt = 0
for i in range(pow(10, k-1), pow(10, k)):
    if math.gcd(i, n) == 1:
        print(i, end=" ")
        cnt += 1
    if cnt == 10:
        cnt = 0
        print()