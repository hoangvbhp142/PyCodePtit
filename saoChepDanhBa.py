class DanhBa:
    def __init__(self, date, name, phoneNum):
        self.date = date.strip()[5:]
        self.name = name.strip()
        self.phoneNum = phoneNum.strip()
        self.tach = self.name.split(" ")

    def __str__(self):
        return f"{self.name}: {self.phoneNum} {self.date}"

    def __lt__(self, other):
        x, y = len(self.tach) - 1, len(other.tach) - 1
        if self.tach[x] < other.tach[y]:
            return self.tach[x] < other.tach[y]
        if self.tach[x] == other.tach[y]:
            return self.tach[0] < other.tach[0]


with open("SOTAY.txt", 'r') as file:
    content = file.readlines()
    cnt = 0
    danhba = []
    a = []
    for i in content:
        if i.strip()[:4] == "Ngay":
            tmp = i
        else:
            a.append(i)
            cnt += 1
        if cnt == 2:
            cnt = 0
            x = DanhBa(tmp, a[0], a[1])
            danhba.append(x)
            a = []
    danhba.sort()
    with open("DIENTHOAI.txt", 'w') as file2:
        for i in danhba:
            file2.write(str(i) + '\n')