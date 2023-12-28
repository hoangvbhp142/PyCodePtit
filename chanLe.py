test = int(input())
while test != 0:
    test -= 1
    n = int(input())
    tong = 0
    ok = True
    while n >= 10:
        so = n % 10
        n //= 10
        tong += so
        if abs(so - n % 10) != 2:
            ok = False
            break
    tong += n
    if ok and tong % 10 == 0:
        print("YES")
    else:
        print("NO")