t = int(input())
for _ in range(t):
    n, m, k = [int(i) for i in input().split()]

    a = sorted([int(i) for i in input().split()])
    b = sorted([int(i) for i in input().split()])
    c = sorted([int(i) for i in input().split()])

    intersection_list = []

    for i in a:
        if (i in b) and (i in c):
            intersection_list.append(i)
    if len(intersection_list) == 0:
        print("NO")
    else:
        for i in intersection_list:
            print(i, end=" ")
        print()