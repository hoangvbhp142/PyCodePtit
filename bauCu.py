n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [0] * (m + 1)
for i in a:
    b[i] += 1
ss = max(b)
zz = min(b[1:])
tt = -1
vitri = -1
for i in range(len(b)):
    if i != 0 and b[i] > tt and b[i] < ss and b[i] > zz:
        tt = b[i]
if tt == -1:
    print("NONE")
else:
    for i in range(len(b)):
        if b[i] == tt:
            print(i)
            break