t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    arr = [int(i) for i in input().split()]
    for i in arr:
        if i not in a:
            a.append(i)
    a.sort()
    l, r = a[0], a[-1]
    print(r - l + 1 - len(a))
