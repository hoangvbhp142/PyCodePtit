nhap = input()
low = 0
up = 0
for i in nhap:
    if i.islower() == True:
        low += 1
    else:
        up += 1
if low >= up:
    print(nhap.lower())
else:
    print(nhap.upper())