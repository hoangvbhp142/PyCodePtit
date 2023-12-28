def check(s):
    if s == s[::-1]:
        return True
    return False

with open("VANBAN.in", 'r') as file:
    dict = {}
    content = file.readlines()
    for i in content:
        line = i.strip().split(" ")
        for j in line:
            if check(j):
                if j not in dict:
                    dict[j] = 1
                else:
                    dict[j] += 1
    tmp = ""
    dem = -1
    for i in dict:
        if len(i) > dem:
            dem = len(i)
            tmp = i
    for i in dict:
        if len(i) == dem:
            print(f"{i} {dict.get(i)}")