def dfs(i, j, res):
    x, y = i, j
    if len(res) == 6:
        res_lst.append(res)
        return

    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, res + arr[nx][ny])

arr = [list(map(str, input().split())) for _ in range(5)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res_lst = []
for i in range(5):
    for j in range(5):
        dfs(i, j, arr[i][j])
res_cnt = len(list(set(res_lst)))
print(res_cnt)
