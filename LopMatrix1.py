test = int(input())
for _ in range(test):
    n, m = [int(i) for i in input().split()]
    a = []
    a_T = []
    for i in range(n):
        a.append([int(number) for number in input().split()])
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