test = int(input())
while test > 0:
    test -= 1
    n = int(input())
    a = [int(number) for number in input().split()]
    sum = 0
    for i in range(3):
        vitri = 0
        max = a[vitri]
        for j in range(1, n):
            if a[j] < a[vitri]:
                vitri = j
        sum += a[vitri]
        a[vitri] = 10**8 + 5
    print(sum)