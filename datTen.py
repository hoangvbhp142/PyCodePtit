def toHopCnk(arr, brr, n, k, j):
    for i in range(brr[j-1] + 1, n - k + j + 1):
        brr[j] = i
        if j == k:
            for x in range(1, k + 1):
                print(arr[brr[x] - 1], end=" ")
            print()
        else:
            toHopCnk(arr, brr, n, k, j+1)


n, k = [int(i) for i in input().split()]
arr = list(set(input().split()))
check = [False] * len(arr)
brr = [0] * (k + 1)
for i in range(k + 1):
    brr[i] = i
arr.sort()
toHopCnk(arr, brr, len(arr), k, 1)