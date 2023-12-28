test = int(input())
while test != 0:
    test -= 1
    nhap = input()
    ok = True
    so1 = nhap[0]
    so2 = nhap[1]
    if so1 == so2:
        print("NO")
    else:
        for i in range(0, len(nhap)):
            if i % 2 == 0 and nhap[i] != so1:
                ok = False
                break
            if i % 2 == 1 and nhap[i] != so2:
                ok = False
                break
        if ok:
            print("YES")
        else:
            print("NO")