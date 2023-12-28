t = int(input())
while t != 0:
    t -= 1
    ok = True
    n = int(input())
    a = [int(number) for number in input().split()]
    b = [int(number) for number in input().split()]
    a.sort()
    b.sort()
    for i in range(n):
        if b[i] < a[i]:
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")