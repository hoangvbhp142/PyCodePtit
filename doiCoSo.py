test = int(input())
for _ in range(test):
    n, k = [int(i) for i in input().split()]
    tmp = ""
    while n != 0:
        x = n % k
        n //= k
        if x < 10:
            tmp = str(x) + tmp
        else:
            tmp = chr(55 + x) + tmp
    print(tmp)