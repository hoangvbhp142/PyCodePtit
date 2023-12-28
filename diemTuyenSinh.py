def chuanhoa(s):
    tach = s.strip().lower().split(" ")
    tmp = ''
    for i in tach:
        if i != '':
            tmp = tmp + i.strip().capitalize() + " "
    return tmp.strip()

class SV:
    def __init__(self, tt, ten, diem, dantoc, khuvuc):
        if tt < 10:
            self.ma = "TS0" + str(tt)
        else:
            self.ma = "TS" + str(tt)
        self.ten = chuanhoa(ten)
        self.diem = diem
        if khuvuc == 1:
            self.diem += 1.5
        if khuvuc == 2:
            self.diem += 1
        if dantoc != "Kinh":
            self.diem += 1.5
        if self.diem >= 20.5:
            self.trangthai = "Do"
        else:
            self.trangthai = "Truot"

    def __str__(self):
        return f"{self.ma} {self.ten} {format(self.diem, '.1f')} {self.trangthai}"


n = int(input())
arr = []
for i in range(n):
    ten = input()
    diem = float(input())
    dantoc = input()
    khuvuc = int(input())
    arr.append(SV(i+1, ten, diem, dantoc, khuvuc))
arr.sort(key=lambda x: x.diem, reverse=True)
for i in arr:
    print(i)

