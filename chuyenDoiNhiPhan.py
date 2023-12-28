import math

f = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
with open("DATA.in", 'r') as file:
    test = int(file.readline().strip())
    for _ in range(test):
        n = int(file.readline().strip())
        xau = file.readline().strip()
        tmp = int(math.log2(n))
        out = ""
        dem = sum = 0
        for i in xau[::-1]:
            if dem == tmp:
                out = f[sum] + out
                dem = 0
                sum = 0
            sum += int(i) * (2 ** dem)
            dem += 1
        if sum != 0:
            out = f[sum] + out
        print(out)