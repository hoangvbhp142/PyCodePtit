class Pair:
    def __init__(self, key, index):
        self.key = key
        self.index = index


n = int(input())
dem = 0
arr = []
stack = []
index = []
for i in range(n):
    arr.append(int(input()))
for i in range(len(arr) - 1, -1, -1):
    while len(stack) != 0 and arr[i] >= stack[-1].key:
        stack.pop(-1)
    if len(stack) == 0:
        index.append(-1)
    else:
        index.append(stack[-1].index)
    stack.append(Pair(arr[i], i))
finalindex = index[::-1]
for i in range(len(finalindex)):
    if finalindex[i] != -1:
        dem += (finalindex[i] - i - 1)
print(dem)
