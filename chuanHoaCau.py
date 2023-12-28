while True:
    while True:
        line = input()
        if line == "":
            break
        line = line.lower().split(" ")
        while line.count("") > 0:
            line.remove("")
        line2 = (' '.join(line)).capitalize()
        n = len(line2)
        if line2[n-1] != '.' and line2[n-1] != '!' and line2[n-1] != '?':
            line2 = line2 + "."
        else:
            if line2[n-2] == " ":
                tmp = line2[:n-2] + line2[n-1]
                line2 = tmp
        print(line2)

