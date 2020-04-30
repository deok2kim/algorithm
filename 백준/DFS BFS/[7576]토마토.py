from collections import deque

garo, sero = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(sero)]

step = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
for i in range(sero):
    for j in range(garo):
        if tomato[i][j] == 1:
            q.append((i, j))

step = 0
while q:
    x, y = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < sero and 0 <= ny < garo:
            if tomato[nx][ny] == 0:
                q.append((nx, ny))
                tomato[nx][ny] = tomato[x][y] + 1
    step = tomato[x][y]
for i in tomato:
    print(i)

for i in tomato:
    if 0 in i:
        step = 0
        break

print(step-1)