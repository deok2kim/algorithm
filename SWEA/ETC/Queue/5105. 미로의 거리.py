T = int(input())
for t in range(1, T + 1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]

    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    q = []
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                q.append([i, j])
                maze[i][j] = 0
                break

    last_cnt = 0
    while q:
        y, x = q.pop(0)
        cnt = maze[y][x] + 1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < N and 0 <= nx < N:
                if maze[ny][nx] == '0':
                    q.append([ny, nx])
                    maze[ny][nx] = cnt
                elif maze[ny][nx] == '3':
                    last_cnt = cnt - 1
                    q.clear()
                    break

    # for m in maze:
    #     print(m)
    print('#{} {}'.format(t, last_cnt))
