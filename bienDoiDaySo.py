while True:
    ok = True
    cnt  = 0
    array = [int(number) for number in input().split()]
    if array.count(0) == 4:
        break
    if array.count(array[0]) == 4:
        print(0)
    else:
        while True:
            ok = True
            tmp = array[0]
            for i in range(len(array) - 1):
                array[i] = abs(array[i] - array[i+1])
            array[3] = abs(array[3] - tmp)
            for i in array:
                if array[0] != i:
                    ok = False
                    break
            cnt += 1
            if ok:
                break
        print(cnt)