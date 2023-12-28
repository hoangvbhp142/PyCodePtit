def chuanhoa(s):
    tmp = s.strip().lower()
    parts = s.split()
    return ' '.join([part.capitalize() for part in parts])


class ThiSinh:
    def __init__(self, tt, ten, diem, dantoc, khuvuc) -> None:
        if tt < 10:
            self.ma = "TS0" + str(tt)
        else:
            self.ma = "TS" + str(tt)
        self.ten = chuanhoa(ten)
        self.diem = diem
        if khuvuc == 1: self.diem += 1.5
        if khuvuc == 2: self.diem += 1.0
        if dantoc != "Kinh": self.diem += 1.5
        if float(self.diem) >= 20.5: self.trangthai = "Do"
        else: self.trangthai = "Truot"

    def __str__(self) -> str:
        return self.ma + " " + self.ten + " " + format(self.diem, ".1f") + " " + self.trangthai
    
    def __lt__(self, other):
        if other.diem > self.diem:
            return other.diem < self.diem
        elif self.diem == other.diem:
            return self.ma < other.ma


n = int(input())
ds = []
for i in range(n):
    ten = input()
    diem = float(input())
    dantoc = input()
    khuvuc = int(input())
    x = ThiSinh(i+1, ten, diem, dantoc, khuvuc)
    ds.append(x)
ds.sort()
for i in ds:
    print(i)