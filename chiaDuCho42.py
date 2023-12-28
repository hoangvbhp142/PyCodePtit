array = []
while len(array) < 10:
    array += [int(number) for number in input().split()]
sett = set()
for i in array:
    sett.add(i % 42)
print(len(sett))