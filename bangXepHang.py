class thanhtich:
    def __init__(self, ten, bailam, submit):
        self.ten = ten
        self.bailam = bailam
        self.submit = submit
    
    def __str__(self):
        return f"{self.ten} {self.bailam} {self.submit}"
    
    def __lt__(self, other):
        if self.bailam > other.bailam:
            return self.bailam > other.bailam
        elif self.bailam == other.bailam:
            if self.submit < other.submit:
                return self.submit < other.submit
            elif  self.submit == other.submit:
                return self.ten < other.ten

n = int(input())
arr = []
for i in range(n):
    ten = input()
    bailam, submit = [int(i) for i in input().split()]
    x = thanhtich(ten, bailam, submit)
    arr.append(x)
arr.sort()
for i in arr:
    print(i)