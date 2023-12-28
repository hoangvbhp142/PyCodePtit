class SoPhuc:
    def __init__(self, phanthuc, phanao):
        self.phanthuc = phanthuc
        self.phanao = phanao

    def __str__(self):
        if self.phanao < 0:
            return f"{self.phanthuc} - {0 - self.phanao}i"
        return f"{self.phanthuc} + {self.phanao}i"

    def __add__(self, other):
        thuc = self.phanthuc + other.phanthuc
        ao = self.phanao + other.phanao
        return SoPhuc(thuc, ao)

    def __mul__(self, other):
        thuc = self.phanthuc * other.phanthuc - self.phanao * other.phanao
        ao = self.phanthuc * other.phanao + self.phanao * other.phanthuc
        return SoPhuc(thuc, ao)

    def spare(self):
        thuc = self.phanthuc ** 2 - self.phanao ** 2
        ao = 2 * self.phanthuc * self.phanao
        return SoPhuc(thuc, ao)

test = int(input())
for _ in range(test):
    a = [int(i) for i in input().split()]
    x1 = SoPhuc(a[0], a[1])
    x2 = SoPhuc(a[2], a[3])
    c = (x1 + x2) * x1
    d = SoPhuc.spare(x1 + x2)
    print(f"{c}, {d}")