test = int(input())
while test != 0:
    test -= 1
    n = input()
    if n[0] == n[len(n) - 1]:
        print("YES")
    else:
        print("NO")