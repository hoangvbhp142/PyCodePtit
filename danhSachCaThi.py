class caThi:
    def __init__(self, i, ngay, gio, id):
        x = str(i)
        while len(x) < 3:
            x = "0" + x
        self.i = 'C' + x
        self.ngay = ngay
        self.gio = gio
        self.id = id
        tmp = ngay.split('/')
        self.ngaydao = tmp[2] + '/' + tmp[1] + '/' + tmp[0]

    def __str__(self):
        return f"{self.i} {self.ngay} {self.gio} {self.id}"
    
    def __lt__(self, other):
        if self.ngaydao < other.ngaydao:
            return self.ngaydao < other.ngaydao
        elif self.ngaydao == other.ngaydao:
            if self.gio < other.gio:
                return self.gio < other.gio
            elif self.gio == other.gio:
                return self.i < other.i
    

with open("CATHI.in") as file:
    n = int(file.readline())
    arr = []
    for i in range(n):
        ngay = file.readline().rstrip()
        gio = file.readline().rstrip()
        id = file.readline().rstrip()
        x = caThi(i+1, ngay, gio, id)
        arr.append(x)
    arr.sort()
    for i in arr:
        print(i)

