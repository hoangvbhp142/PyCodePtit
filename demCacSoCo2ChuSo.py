dict = {}
n = input()
dem = 0
tmp = ""
for i in n:
    tmp = tmp + i
    if len(tmp) == 2:
        if int(tmp) not in dict:
            dict[int(tmp)] = 1
        else:
            dict[int(tmp)] += 1
        tmp = ""
for i in dict:
    print(f"{i} {dict[i]}")