test = int(input())
for _ in range(test):
    s = input()
    tmp1, tmp2, tmp  = "", "", ""
    rolate1, rolate2 = 0, 0
    phan1 = s[:len(s) // 2]
    phan2 = s[len(s) // 2:]
    for i in range(int(len(s) // 2)):
        rolate1 += (ord(phan1[i]) - 65)
        rolate2 += (ord(phan2[i]) - 65)
    for i in range(int(len(s) // 2)):
        tmp1 = tmp1 + chr(((ord(phan1[i]) - 65 + rolate1) % 26) + 65)
        tmp2 = tmp2 + chr(((ord(phan2[i]) - 65 + rolate2) % 26) + 65)
    for i in range(int(len(s) // 2)):
        tmp = tmp + chr( ( ord(tmp1[i]) + ord(tmp2[i]) - 2 * 65) % 26 + 65 )
    print(tmp)