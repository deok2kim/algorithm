m, n, k = map(int, input().split())
paper = [[0]*n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            paper[i][j] += 1

for i in paper:
    print(i)
result = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(m):
    for j in range(n):
        cnt = 0
        if paper[i][j] == 0:
            stack = [(i, j)]
            paper[i][j] = -1

            while stack:
                x, y = stack.pop()
                cnt += 1
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < m and 0<= ny < n:
                        if paper[nx][ny] == 0:
                            stack.append((nx, ny))
                            paper[nx][ny] = -1

            result.append(cnt)

result.sort()
print(len(result))
print(' '.join(list(map(str, result))))
