class TienNuoc:

    def __init__(self, ma, ten, socu, somoi):
        self.ma = ma
        self.ten = ten
        self.sonuoc = somoi - socu

        if self.sonuoc <= 50:
            self.tongtien = self.sonuoc * 100 * 1.02
        elif self.sonuoc <= 100:
            self.tongtien = ((self.sonuoc - 50) * 150 + 50 * 100) * 1.03
        else:
            self.tongtien = ((self.sonuoc - 100) * 200 + 50 * 250) * 1.05

        self.tongtien = round(self.tongtien)

    def __str__(self):
        return f"{self.ma} {self.ten} {self.tongtien}"

    def output(self):
        print(self.ma, self.ten, self.tongtien)


t = int(input())
a = []
for i in range(t):
    ma = "KH{:02d}".format(i+1)
    ten = input()
    socu = int(input())
    somoi = int(input())
    x = TienNuoc(ma, ten, socu, somoi)
    a.append(x)
a.sort(key=lambda x: x.tongtien, reverse=True)
for i in a:
    i.output()
"""
3
Le Thi Thanh
468
500
Le Duc Cong
160
230
Ha Hue Anh
410
612
"""