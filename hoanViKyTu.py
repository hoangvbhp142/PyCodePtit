def hoanvi(s, a, out, check, n, i):
    for j in range(1, n + 1):
        if check[j] == 0:
            out[i] = j
            check[j] = 1
            if i == n:
                for i in range(1, n + 1):
                    print(s[out[i] - 1], end = "")
                print()
            else:
                hoanvi(s, a, out, check, n, i+1)
            check[j] = 0

s = input()
n = len(s)
a = [0] * (n + 1)
out = [0] * (n + 1)
check = [0] * (n + 1)
for i in range(0, n + 1):
    a[i] = i
hoanvi(s, a, out, check, n, 1)