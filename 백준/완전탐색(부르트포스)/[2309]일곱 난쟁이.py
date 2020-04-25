dwarfs = [int(input()) for x in range(9)]

total = sum(dwarfs)
for i in range(9):
    for j in range(i+1,9):
        a = dwarfs[i]
        b = dwarfs[j]
        if total - (a + b) == 100:
            dwarfs.remove(a)
            dwarfs.remove(b)
            break

    if len(dwarfs) == 7:
        break

dwarfs.sort()
for dwarf in dwarfs:
    print(dwarf)
