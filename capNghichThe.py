n = input()
array = [int(number) for number in input().split()]
sum = 0
for i in range(1, len(array)):
    for j in range(0, i):
        if array[j] > array[i]:
            sum += 1
print(sum)