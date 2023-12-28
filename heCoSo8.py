dem = 3
so = 0
xau2 = input()
xau8 = ""
n = len(xau2)
if n % 3 != 0:
    xau2 = (3 - n % 3) * "0" + xau2
for i in xau2:
    dem -= 1
    so = so + int(i) * (2 ** dem)
    if dem <= 0:
        xau8 = xau8 + str(so)
        so = 0
        dem = 3
print(xau8)