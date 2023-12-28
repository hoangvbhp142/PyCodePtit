test = int(input())
while test != 0:
    test -= 1
    n = int(input())
    lan = 2
    print("1 ", end="")
    while(n != 1):
        dem = 0
        while n % lan == 0:
            n /= lan
            dem += 1
        if dem != 0:
            print(f"* {lan}^{dem}", end=" ")
        lan += 1
    print()
        
