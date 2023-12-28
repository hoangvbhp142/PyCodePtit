import math        

mydict = {
    "0":"0", "1":"1", "2":"2", "3":"3", "4":"4", "5":"5", "6":"6", "7":"7", "8":"8", "9":"9",
    "10":"A", "11":"B", "12":"C", "13":"D", "14":"E", "15":"F"
}
test = int(input())
while test != 0:
    test -= 1
    coso = int(input())
    xau = input()[::-1]
    if len(xau) % int(math.log2(coso)) != 0:
        xau = xau + '0' * (int(math.log2(coso)) - len(xau) % int(math.log2(coso)))
    out = ""
    so = lan = 0
    for i in xau:
        if i == '1':
            so += 2 ** lan
        lan += 1
        if lan == int(math.log2(coso)):
            out = mydict[str(so)] + out
            lan = 0
            so = 0
    print(out)