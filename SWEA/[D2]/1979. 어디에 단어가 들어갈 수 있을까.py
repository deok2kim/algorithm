T = int(input())

for t in range(1, T + 1):
    n, k = map(int, input().split())
    puzzle = [ list(map(int, input().split())) for _ in range(n) ]

    tot = 0
    for i in range(n):
        for j in range(n):
            if puzzle[i][j] == 1:
                xcnt = 1
                ycnt = 1
                x = j
                y = i
                # 가로확인
                while True:
                    if j - 1 == -1 or puzzle[i][j - 1] == 0:
                        x = x + 1
                        if x < n and puzzle[i][x] == 1:
                            xcnt += 1
                        else:
                            break
                    else:
                        break

                if xcnt == k:
                    tot += 1

                while True:
                    if i - 1 == -1 or puzzle[i - 1][j] == 0:
                        y = y + 1
                        if y < n and puzzle[y][j] == 1:
                            ycnt += 1
                        else:
                            break
                    else:
                        break
                if ycnt == k:
                    tot += 1

    print('#{} {}'.format(t, tot))
