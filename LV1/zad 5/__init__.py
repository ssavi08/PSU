fopen = open('song.txt')

rijeci = {}

for linija in fopen:
    linija = linija.split(" ")
    for rijec in linija:
        rijec = rijec.rstrip('\n').replace(",", "")

        if rijec.lower() in rijeci:
            rijeci[rijec.lower()] += 1
        else:
            rijeci[rijec.lower()] = 1

print(rijeci)
br = 0
for x in rijeci:
    if rijeci.get(x) == 1:
        br = br + 1

print(f"{br} rijeci se ponavlja jedanput")