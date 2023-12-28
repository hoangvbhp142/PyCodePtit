test = int(input())
while test != 0:
    test -= 1
    nhap = input()
    ok = True
    for i in nhap:
        if i != '0' and i != '1' and i != '2':
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")