def recur(before, cur_battery):
    global min_battery

    if False not in visit:
        min_battery = min(min_battery, cur_battery)
        return

    if cur_battery > 0 and before == 0:
        return

    for i in range(n):
        if visit[i] is False and before != i:
            visit[i] = True
            result[i] = golf[before][i]
            recur(i, cur_battery + golf[before][i])
            visit[i] = False

    return


for tc in range(int(input())):
    n = int(input())
    golf = [list(map(int, input().split())) for _ in range(n)]

    visit = [False] * n
    result = [0]*n
    min_battery = 1000

    recur(0, 0)
    print('#{} {}'.format(tc+1, min_battery))
