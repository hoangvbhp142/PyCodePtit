while True:
    n = int(input())
    if n == 0:
        break
    a = []
    for _ in range(n):
        a.append(int(input()))
    a.sort()
    if a[0] == a[n-1]:
        print("BANG NHAU")
    else:
        print(f"{a[0]} {a[n-1]}")
