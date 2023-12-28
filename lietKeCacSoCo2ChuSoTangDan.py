n = input()
a = []
tmp = ""
for i in n:
    tmp = tmp + i
    if len(tmp) == 2:
        if int(tmp) not in a:
            a.append(int(tmp))
        tmp = ""
#a.sort()
for i in a:
    print(i, end=" ")
print()