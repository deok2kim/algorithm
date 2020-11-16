from itertools import combinations
from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for tc in range(1, 1 + int(input())):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    answer = []
    restaurants = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] > 1:
                restaurants.append((i, j))

    for n in range(1, len(restaurants) + 1):
        for R in combinations(restaurants, n):

            key = [[0] * N for _ in range(N)]
            result = 0
            for r in R:
                visited = [[0] * N for _ in range(N)]
                q = deque()
                q.append(r)
                visited[r[0]][r[1]] = 1
                key[r[0]][r[1]] = 0
                result += maps[r[0]][r[1]]
                while q:
                    cx, cy = q.popleft()

                    for k in range(4):
                        nx = cx + dx[k]
                        ny = cy + dy[k]
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                            if key[nx][ny] > key[cx][cy] + 1 or key[nx][ny] == 0:
                                key[nx][ny] = key[cx][cy] + 1
                                q.append((nx, ny))
                            visited[nx][ny] = 1

            # 비용 계산

            for i in range(N):
                for j in range(N):
                    if maps[i][j] == 1:
                        result += key[i][j]

            answer.append(result)

    print(f'#{tc} {min(answer)}')
