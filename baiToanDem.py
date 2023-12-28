n = int(input())
a = []
d = []
while len(a) < n:
    tmp = [int(i) for i in input().split()]
    a.extend(tmp)
ok = True
for i in range(1, a[-1] + 1):
    if i not in a:
        print(i)
        ok = False
if ok:
    print("Excellent!")
