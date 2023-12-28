with open("DATA.in") as file:
    content = file.readlines()
    a = []
    for i in content:
        x = i.strip().split()
        for j in x:
            try:
                n = int(j)
                if n > 2147483647:
                    a.append(j)
            except:
                a.append(j)
    a.sort()
    for i in a:
        print(i, end = " ")
    print()