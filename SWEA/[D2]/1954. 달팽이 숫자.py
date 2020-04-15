T = int(input())
for t in range(1, T + 1):
    n = int(input())
    snail = [[0]*n for _ in range(n)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    k, y, x = 0, 0, 0

    num = 1
    snail[y][x] = num

    while num != n ** 2:
        if 0 <= x + dx[k] < n and 0 <= y + dy[k] < n:
            x += dx[k]
            y += dy[k]

            if snail[y][x] == 0:
                num += 1
                snail[y][x] = num

            else:
                x -= dx[k]
                y -= dy[k]
                k += 1
                k = k % 4
        else:
            k += 1
            k = k % 4

    print('#{}'.format(t))
    for i in snail:
        print(' '.join(list(map(str, i))))
