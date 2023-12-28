def C2n(n):
    if n < 2:
        return 0
    return n * (n - 1) // 2

n = int(input())
tong = 0
a = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    a[i] = input()
for i in range(n):
    tong += C2n(a[i].count('C'))
    cnt = 0
    for j in range(n):
        if a[j][i] == 'C':
            cnt += 1
    tong += C2n(cnt)
print(tong)
