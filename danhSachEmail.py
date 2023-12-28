file = open('CONTACT.in', 'r')
content = file.readlines()
myDict = []
for i in content:
    x = i.split('\n')
    if x[0].lower() not in myDict:
        myDict.append(x[0].lower())
myDict.sort()
for i in myDict:
    print(f"{i}")