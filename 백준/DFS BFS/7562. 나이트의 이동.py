from collections import deque


def bfs():
    q = deque()
    q.append((start_x, start_y))
    while q:
        cx, cy = q.popleft()
        if cx == end_x and cy == end_y:
            print(chess[cx][cy])
            return
        for k in range(len(dx)):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < N and 0 <= ny < N and chess[nx][ny] == '':
                chess[nx][ny] = chess[cx][cy] + 1
                if nx == end_x and ny == end_y:
                    print(chess[nx][ny])
                    return

                q.append((nx, ny))


for tc in range(int(input())):
    N = int(input())
    chess = [[''] * N for _ in range(N)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    chess[start_x][start_y] = 0
    dx, dy = [-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]
    bfs()
