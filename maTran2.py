n = int(input())
matran = [[0 for j in range(n)] for i in range(n)]
tren = 0
duoi = 0
for i in range(n):
    matran[i] = [int(number) for number in input().split()]
    for j in range(n):
        if i + j > n - 1:
            duoi += matran[i][j]
        elif i + j < n - 1:
            tren += matran[i][j]
k = int(input())
if abs(tren - duoi) <= k:
    print("YES")
else:
    print("NO")
print(abs(tren - duoi))