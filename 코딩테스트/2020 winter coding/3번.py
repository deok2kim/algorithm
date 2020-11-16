from collections import deque


def bfs(x, y, farm):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    n = len(farm)
    q = deque()
    q.append((x, y))
    crop = farm[x][y]
    farm[x][y] = 9  # 방문의 의미
    while q:
        cx, cy = q.popleft()
        for k in range(len(dx)):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if farm[nx][ny] == crop:
                    q.append((nx, ny))
                    farm[nx][ny] = 9


def solution(v):
    answer = [0, 0, 0]
    n = len(v)

    for i in range(n):
        for j in range(n):
            if v[i][j] != 9:
                answer[v[i][j]] += 1
                bfs(i, j, v)
    return answer


print(solution([[0, 0, 1, 1], [1, 1, 1, 1], [2, 2, 2, 1], [0, 0, 0, 2]]))
