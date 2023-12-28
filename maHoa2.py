T = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    nhap = input().split()
    k = int(nhap[0])
    if k == 0:
        break
    s = str(nhap[1])
    out = ""
    for i in s:
        vitri = int(T.index(i))
        out =T[(vitri + k) % 28] + out
    print(out)