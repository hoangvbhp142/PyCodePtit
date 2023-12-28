while True:
    num = int(input())
    if num == 0:
        break
    cnt = 1
    while num != 1:
        cnt += 1
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
    print(cnt)