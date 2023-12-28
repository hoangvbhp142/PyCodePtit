test = int(input())
for _ in range(test):
    nhap = []
    while len(nhap) < 2:
        nhap += [int(number) for number in input().split()]
    n, m = nhap
    a = []
    a_T = []
    for i in range(n):
        draft = []
        while len(draft) < m:
            draft += [int(number) for number in input().split()]
        a.append(draft)
    for i in range(m):
        tmp = []
        for j in range(n):
            tmp.append(a[j][i])
        a_T.append(tmp)
    for i in range(n):
        for j in range(n):
            res = 0
            for k in range(m):
                res += a[i][k] * a_T[k][j]
            print(res, end=" ")
        print()