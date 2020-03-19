n = int(input())
tile = [0] * (n + 1)
tile[1] = 1
for i in range(2, n + 1):
    if i % 2 == 0:
        tile[i] = tile[i - 1] * 2 + 1
    else:
        tile[i] = tile[i - 1] * 2 - 1

print(tile[-1] % 10007)
