dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for _ in range(10):
    answer = 0
    n = int(input())
    N = 100
    maps = [list(input()) for _ in range(N)]

    # 출발점 찾기
    x, y = 0, 0
    for i in range(N):
        for j in range(N):
            if maps[i][j] == '2':
                x, y = i, j

    # 미로탐색 DFS
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                # 길을 만날 경우
                if maps[nx][ny] == '0':
                    stack.append((nx, ny))
                    maps[nx][ny] = '9'
                # 끝점을 만날 경우
                elif maps[nx][ny] == '3':
                    answer = 1
                    stack.clear()
                    break

    print('#{} {}'.format(n, answer))
