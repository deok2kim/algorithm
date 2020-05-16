def backt(idx, total):
    global result
    if sum(visit) == n:
        result = min(result, total)
        return

    if total > result:
        return

    for i in range(n):
        if visit[i] == 0:
            visit[i] = 1
            backt(idx+1, total+prices[idx][i])
            visit[i] = 0

    return


for tc in range(int(input())):
    n = int(input())
    prices = [list(map(int, input().split())) for _ in range(n)]

    visit = [0]*n
    result = 99*n
    backt(0, 0)

    print('#{} {}'.format(tc+1, result))
