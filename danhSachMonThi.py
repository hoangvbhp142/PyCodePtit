class MonThi:

    def __init__(self, ma, ten, hinhthuc):
        self.ma = ma
        self.ten = ten
        self.hinhthuc = hinhthuc

    def __str__(self):
        return f"{self.ma} {self.ten} {self.hinhthuc}"


n = int(input())
arr = []
for i in range(n):
    ma = input()
    ten = input()
    hinhthuc = input()
    arr.append(MonThi(ma, ten, hinhthuc))

arr.sort(key=lambda x: x.ma)
for i in arr:
    print(i)

