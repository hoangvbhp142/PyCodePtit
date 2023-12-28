from math import *

class PhanSo:
    def __init__(self, tu, mau):
        x = gcd(tu, mau)
        self.tu = tu // x
        self.mau = mau // x
    
    def __str__(self) -> str:
        return f"{self.tu}/{self.mau}"
    
    def tinhtong(self, other):
        m = self.mau * other.mau
        t = self.tu * other.mau + self.mau * other.tu
        tong = PhanSo(t, m)
        return tong

arr = [int(i) for i in input().split()]
p1 = PhanSo(arr[0], arr[1])
p2 = PhanSo(arr[2], arr[3])
print(p1.tinhtong(p2))