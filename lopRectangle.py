class Rectangle:
    def __init__(self, dai, rong, mau):
        self.dai = dai
        self.rong = rong
        self.mau = mau
    
    def perimeter(self):
        return (self.rong + self.dai) * 2
    
    def area(self):
        return self.dai * self.rong
    
    def color(self):
        return self.mau.title()

arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print("INVALID")