from copy import deepcopy
def dfs(rgb):
    dy = [-1, 1, 0, 0]  # 상 하 좌 우
    dx = [0, 0, -1, 1]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if rgb[i][j] != 0:
                color = rgb[i][j]
                stack = [(i, j)]
                cnt += 1
                rgb[i][j] = 0
                while stack:
                    y, x = stack.pop()

                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if 0 <= ny < n and 0 <= nx < n:
                            if rgb[ny][nx] == color:
                                stack.append((ny, nx))
                                rgb[ny][nx] = 0
    return cnt


n = int(input())
data = [list(input()) for _ in range(n)]
data2 = deepcopy(data)
for i in range(n):
    for j in range(n):
        if data[i][j] == 'R' or data[i][j] == 'G':
            data2[i][j] = 'RG'
        else:
            data2[i][j] = 'B'
rgb_cnt = dfs(data)
rgb_blind_cnt = dfs(data2)
print(rgb_cnt, rgb_blind_cnt)
