test = int(input())
while test != 0:
    test -= 1
    num = input()
    dao = num[::-1]
    lan = 0
    while lan < 1000:
        if int(num) % 7 == 0:
            print(num)
            break
        lan += 1
        num = int(num) + int(dao)
        dao = str(num)[::-1]
    if lan == 1000:
        print(-1)

