class BangDiem:
    def __init__(self, mhs, ten, diem):
        if mhs < 10:
            x = "0" + str(mhs)
        else:
            x = str(mhs)
        self.mhs = "HS" + x
        self.ten = ten
        self.tb = diem[0] * 2.0 + diem[1] * 2.0
        for i in range(2, 10):
            self.tb += diem[i]
        self.tb = self.tb / 10 / 1.2

        if self.tb >= 9.0:
            self.hocluc = "XUAT SAC"
        elif self.tb >= 8.0:
            self.hocluc = "GIOI"
        elif self.tb >= 7.0:
            self.hocluc = "KHA"
        elif self.tb >= 5.0:
            self.hocluc = "TB"
        else:
            self.hocluc = "YEU"

    def __str__(self):
        return f"{self.mhs} {self.ten} {format(self.tb, '.1f')} {self.hocluc}"

    def __lt__(self, other):
        if self.tb > other.tb:
            return self.tb > other.tb
        elif self.tb == other.tb:
            return self.mhs < other.mhs
        
n = int(input())
list = []
for _ in range(n):
    ten = input()
    diem = [float(i) for i in input().split()]
    list.append(BangDiem(_ + 1, ten, diem))
list.sort()
for i in list:
    print(i)