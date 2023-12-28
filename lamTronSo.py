test = int(input())
while test != 0:
    test = int(test) - 1
    num = input()
    if len(num) < 2:
        print(num)
    else:
        if num[0] == '9':
            num = "0" + num
        num = list(num)
        start = len(num)
        nho = 0
        while start > 0:
            start -= 1
            so = int(num[start]) + nho
            if so >= 5:
                nho = 1
            else:
                nho = 0
            if start != 0:
                num[start] = '0'
            else:
                num[start] = str(so)
        print("".join(num))
            
            
        