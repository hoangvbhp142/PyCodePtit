class ThiSinh:
    def __init__(self, ten, ngaysinh, p1, p2, p3):
        self.ten = ten
        self.ngaysinh = ngaysinh
        self.tongdiem = round(p1 + p2 + p3, 1)

    def __str__(self):
        return f"{self.ten} {self.ngaysinh} {self.tongdiem}"


ten = input()
ngaysinh = input()
p1 = float(input())
p2 = float(input())
p3 = float(input())
print(ThiSinh(ten, ngaysinh, p1, p2, p3))