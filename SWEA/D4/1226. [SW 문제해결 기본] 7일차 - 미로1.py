dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for _ in range(10):
    answer = 0
    n = int(input())
    maps = [list(input()) for _ in range(16)]

    # 출발점 찾기
    x, y = 0, 0
    for i in range(16):
        for j in range(16):
            if maps[i][j] == '2':
                x, y = i, j

    # 미로탐색 DFS
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < 16 and 0 <= ny < 16:
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
