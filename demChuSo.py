test = int(input())
for _ in range(test):
    a, b = [int(i) for i in input().split()]
    dem = [0 for i in range(10)]
    for i in range(a, b+1):
        tmp = str(i)
        if len(tmp) % 2 != 0:
            tmp = tmp + "."
        for j in range(0, len(tmp)//2):
            try:
                x = int(tmp[j])
                dem[x] += 1
            except ValueError:
                pass
            try:
                x = int(tmp[len(tmp) - 1 - j])
                dem[x] += 1
            except ValueError:
                pass
    for i in range(10):
        print(dem[i], end=" ")
    print()