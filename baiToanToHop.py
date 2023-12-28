def tohop(a, array, out, n, k, i):
    for j in range(a[i-1] + 1, n - k + i + 1):
        a[i] = j
        out[i] = array[a[i]]
        if i == k:
            for x in range(1, len(out)):
                print(out[x], end = " ")
            print()
        else:
            tohop(a, array, out, n, k, i+1)


a = [0] * 1005
nhap = input().split()
nhap = [int(number) for number in nhap]
n, k = nhap
nhap2 = input().split()
nhap2 = [int(number) for number in nhap2]
array = [0]
for i in nhap2:
    if a[i] == 0:
        array.append(i)
        a[i] = 1
array.sort()
b = [0] * len(array)
out = [0] * (k+1)
for i in range(0, len(array)):
    b[i] = i
tohop(b, array, out, len(array) - 1, k, 1)
