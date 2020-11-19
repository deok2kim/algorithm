from collections import deque


def find_balls():
    # 최초 red, blue 공 찾기
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'R':
                rx, ry = i, j
            elif maps[i][j] == 'B':
                bx, by = i, j

    return rx, ry, bx, by


def move_ball(x, y, mx, my, cnt=0):
    while True:
        if maps[x + mx][y + my] == '#' or maps[x][y] == 'O':
            return x, y, cnt
        x += mx
        y += my
        cnt += 1


def bfs():
    # 기울이기(이동하기)
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상 하 좌 우
    while q:
        rx, ry, bx, by, c = q.popleft()

        if c >= 10:
            return -1
        for k in range(len(dx)):
            nrx, nry, rc = move_ball(rx, ry, dx[k], dy[k])
            nbx, nby, bc = move_ball(bx, by, dx[k], dy[k])

            # 만약 파란공이 들어간다면 실패이므로
            if maps[nbx][nby] == 'O':
                continue
            # 만약 파란공은 안들어갔지만 빨간공만들어가면 성공!
            elif maps[nrx][nry] == 'O':
                return c + 1

            # 만약 겹칠 경우 더 적게 이동한 공이 더 앞에 있다.
            if nrx == nbx and nry == nby:
                if rc > bc:  # blue가 더 적게 이동, blue가 앞
                    nrx -= dx[k]
                    nry -= dy[k]
                else:
                    nbx -= dx[k]
                    nby -= dy[k]

            key = (nrx, nry, nbx, nby)
            if maps[nbx][nby] != 'O' and not check.get(key):  # 파란공이 구멍에 들어가면 이 경우는 더 이상 진행하지 않는다.
                q.append(key + (c + 1,))
                check[key] = 1
    return -1


if __name__ == '__main__':
    N, M = map(int, input().split())
    maps = [list(input()) for _ in range(N)]

    check = {}
    q = deque()

    rx, ry, bx, by = find_balls()
    q.append((rx, ry, bx, by, 0))
    check[(rx, ry, bx, by)] = 1
    answer = bfs()
    print(answer)
