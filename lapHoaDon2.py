from datetime import datetime

giatien = [25, 34, 50, 80]

class TinhTien:

    def __init__(self, ma, ten, sophong, ngaynhan, ngaytra, phatsinh):
        self.ma = "KH{:02d}".format(ma + 1)
        self.ten = ten
        nhan = datetime(year=ngaynhan[2], month=ngaynhan[1], day=ngaynhan[0])
        tra = datetime(year=ngaytra[2], month=ngaytra[1], day=ngaytra[0])
        self.ngay = (tra - nhan).days
        self.phong = sophong // 100
        self.tongtien = giatien[self.phong - 1] * self.ngay + phatsinh





t = int(input())
for i in range(t):
    ten = input()
    sophong = int(input())
    ngaynhan = [int(i) for i in input().split('/')]
    ngaytra = [int(i) for i in input().split('/')]
    phatsinh = int(input())
