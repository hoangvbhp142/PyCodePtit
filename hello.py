num = int(input())
so4 = 0
so7 = 0
while num != 0:
    if num % 10 == 4:
        so4 = so4 + 1
    if num % 10 == 7:
        so7 = so7 + 1
    num = num // 10
so = so4 + so7
if (so == 4 or so == 7):
    print("YES")
else:
    print("NO")
