if __name__ == "__main__":
    r, c = map(int, input().split())
    robot = tuple(map(int, input().split()))
    room = [list(map(int, input().split())) for _ in range(r)]

    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    #       0, 1, 2, 3
    # 방향은 북 동 남 서

    #       0, 3, 2, 1
    # 탐색은 북 서 남 동
    q = [robot]
    cnt = 0
    while q:
        x, y, d = q.pop()
        if room[x][y] == 0:
            room[x][y] = 2
            cnt += 1

        for k in range(d - 1, d - 1 - 4, -1):
            k += 4
            k %= 4
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < r and 0 <= ny < c:
                if room[nx][ny] == 0:
                    q.append((nx, ny, k))
                    break
        else:
            nd = (d + 2) % 4
            nx = x + dx[nd]
            ny = y + dy[nd]
            if 0 <= nx < r and 0 <= ny < c:
                if room[nx][ny] == 1:
                    break
                else:
                    q.append((nx, ny, d))

    print(cnt)
