t = int(input())
for _ in range(t):
    n = input().split('.')
    if len(n) != 4:
        print("NO")
    else:
        ok = True
        for i in n:
            try:
                tmp = int(i)
                if tmp > 255 or tmp < 0:
                    ok = False
                    break
            except Exception:
                ok = False
                break
        if ok:
            print("YES")
        else:
            print("NO")