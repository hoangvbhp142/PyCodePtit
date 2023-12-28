test = int(input())
while test != 0:
    test -= 1
    nhap = input()
    xuat = ""
    for i in range(1, len(nhap)):
        xau = nhap[i-1]
        if nhap[i].isnumeric():
            xuat = xuat + str(xau) * int(nhap[i])
    print(xuat)