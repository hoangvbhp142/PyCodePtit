
List = list(map(int, input().split()))
a, k, n = List
left = a // k + 1
right = n // k + 1
if left >= right:
    print(-1)
else:
    for i in range(left, right):
        print(i * k - a, end=" ")