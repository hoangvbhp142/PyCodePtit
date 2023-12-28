from math import *

class Point:
    def __init__(self, x, y) :
        self.x = x
        self.y = y
    def distance(self, other):
        return sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))

class Triangle:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
    def __str__(self):
        AB = (self.A).distance(self.B)
        AC = (self.A).distance(self.C)
        BC = (self.C).distance(self.B)
        if AB + AC <= BC or BC + AC <= AB or AB + BC <= AC:
            return "INVALID"
        else:
            p = (AB + AC + BC) / 2
            return "{:.2f}".format(sqrt(p * (p - BC) * (p - AB) * (p -AC)))

t = int(input())
lst = list()
for _ in range(t):
    while True:
        if len(lst) >= 6:
            break
        lst.extend([float(x) for x in input().split()])
    A = Triangle(Point(lst[0], lst[1]), Point(lst[2], lst[3]), Point(lst[4], lst[5]))
    print(A)
    x = lst[6:]
    lst = x