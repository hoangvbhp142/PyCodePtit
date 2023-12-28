test = int(input())
while test != 0:
    test -= 1
    nhap = input()
    dau = int(nhap[0:2])
    cuoi = int(nhap[len(nhap)-2:])
    if dau == cuoi:
        print("YES")
    else:
        print("NO")
    
