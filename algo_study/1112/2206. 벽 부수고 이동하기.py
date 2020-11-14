from collections import deque

if __name__ == '__main__':
    N, M = map(int, input().split())
    field = [list(input()) for _ in range(N)]
    for row in field:
        print(row)
    print()

    visited = [[0] * M for _ in range(N)]

    q = deque()
    q.append((0, 0, 0, 0))  # 벽을 부쉈으면 마지막은 1
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        x, y, cost, B = q.popleft()
        if x == N - 1 and y == M - 1:
            print(cost + 1)
            break
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if field[nx][ny] == '1':  # 벽일 때
                    if B == 0:  # 벽을 뚫은 적이 없을 떄만 고
                        q.append((nx, ny, cost + 1, 1))
                        visited[nx][ny] = 1
                else:
                    q.append((nx, ny, cost + 1, B))
                    visited[nx][ny] = 1

    else:
        print(-1)
