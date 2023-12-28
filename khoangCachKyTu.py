def solve(s1):
    s2 = s1[::-1]
    for i in range(1, len(s1) - 1):
        if abs(ord(s1[i]) - ord(s1[i-1])) != abs(ord(s2[i]) - ord(s2[i-1])):
            return False
    return True

test = int(input())
while test != 0:
    test -= 1
    s1 = input()
    if solve(s1):
        print("YES")
    else:
        print("NO")