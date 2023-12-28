test = int(input())
while test != 0:
    test -= 1
    dem = 0
    nhap = input() + "*"
    mau = nhap[0]
    output = ""
    for i in range(0, len(nhap)):
        if mau == nhap[i]:
            dem += 1
        else:
            output = output + str(dem) + mau
            mau = nhap[i]
            dem = 1
    print(output)