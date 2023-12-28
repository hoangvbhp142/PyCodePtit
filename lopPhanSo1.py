from math import *

class PhanSo:
    def __init__(self, tu, mau):
        x = gcd(tu, mau)
        self.tu = tu // x
        self.mau = mau // x
    
    def __str__(self) -> str:
        return f"{self.tu}/{self.mau}"
    
tu, mau = [int(i) for i in input().split()]
phanso = PhanSo(tu, mau)
print(phanso)
    