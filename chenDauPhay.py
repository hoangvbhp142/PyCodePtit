nhap = input()
out = ""
dem = 0
nhap = nhap[::-1]
for i in nhap:
    dem += 1
    out = i + out
    if dem == 3:
        out = ',' + out
        dem = 0
if out[0] == ',':
    out = out[1:]
print(out)