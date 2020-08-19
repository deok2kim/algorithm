def dfs(idx, cal, lmt, o_cal):
    global result
    if lmt > l:
        if o_cal > result:
            result = o_cal
        return
    if idx == n:
        if cal > result:
            result = cal
        return

    for i in range(idx, n):
        dfs(i + 1, cal + burger[i][0], lmt + burger[i][1], cal)

    return


T = int(input())
for t in range(1, T + 1):
    n, l = map(int, input().split())
    burger = [list(map(int, input().split())) for _ in range(n)]
    visit = [False]*n
    result = 0
    dfs(0, 0, 0, 0)
    print('#{} {}'.format(t, result))
