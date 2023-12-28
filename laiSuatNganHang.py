import math
test = int(input())
while test != 0:
    test -= 1
    nhap = input()
    nhap = nhap.split(" ")
    n, x, m = nhap
    n = float(n)
    x = float(x) / 100
    m = float(m)
    nam = math.log10(m / n) / math.log10(1 + x)
    nam = math.ceil(nam)
    print(int(nam))