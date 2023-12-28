import math

def check(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True

n, m = [int(number) for number in input().split()]
matrix = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    matrix[i] = [int(number) for number in input().split()]
    for j in range(m):
        if check(matrix[i][j]):
            matrix[i][j] = 1
        else:
            matrix[i][j] = 0
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end = " ")
    print()
    