n = int(input())
array = [int(number) for number in input().split()]
sum = 0
for i in range(n-1):
    if array[i] != array[i+1]:
        sum += 1
print(sum)