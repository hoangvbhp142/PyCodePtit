fibo = [0] * 95
fibo[0] = 0
fibo[1] = 1
for i in range(2, 94):
    fibo[i] = fibo[i-1] + fibo[i-2]

test = int(input())
while test != 0:
    test -= 1
    a, b = [int(number) for number in input().split()]
    for i in range(a, b+1):
        print(fibo[i], end = " ")
    print()
