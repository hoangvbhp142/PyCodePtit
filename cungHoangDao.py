test = int(input())
for i in range(0, test):
    nhap = input().split()
    nhap = [int(number) for number in nhap]
    day, month = nhap
    if ((day in range(21, 32)) and month == 3) or ((day in range(1, 20)) and month == 4):
        print("Bach Duong")
    if ((day in range(20, 31)) and month == 4) or ((day in range(1, 21)) and month == 5):
        print("Kim Nguu")
    if ((day in range(21, 32)) and month == 5) or ((day in range(1, 21)) and month == 6):
        print("Song Tu")
    if ((day in range(21, 31)) and month == 6) or ((day in range(1, 23)) and month == 7):
        print("Cu Giai")
    if ((day in range(23, 32)) and month == 7) or ((day in range(1, 23)) and month == 8):
        print("Su Tu")
    if ((day in range(23, 32)) and month == 8) or ((day in range(1, 23)) and month == 9):
        print("Xu Nu")
    if ((day in range(23, 31)) and month == 9) or ((day in range(1, 23)) and month == 10):
        print("Thien Binh")
    if ((day in range(23, 32)) and month == 10) or ((day in range(1, 23)) and month == 11):
        print("Thien Yet")
    if ((day in range(23, 31)) and month == 11) or ((day in range(1, 22)) and month == 12):
        print("Nhan Ma")
    if ((day in range(22, 32)) and month == 12) or ((day in range(1, 20)) and month == 1):
        print("Ma Ket")
    if ((day in range(20, 32)) and month == 1) or ((day in range(1, 19)) and month == 2):
        print("Bao Binh")
    if ((day in range(19, 32)) and month == 2) or ((day in range(1, 21)) and month == 3):
        print("Song Ngu")